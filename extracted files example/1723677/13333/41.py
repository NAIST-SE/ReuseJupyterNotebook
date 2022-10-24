class DataGenerator2(keras.utils.Sequence):
    # USES GLOBAL VARIABLE TRAIN2 COLUMNS E1, E2, E3, E4
    'Generates data for Keras'
    def __init__(self, list_IDs, batch_size=24, shuffle=False, width=544, height=352, scale=1/128., sub=1., mode='train_seg',
                 path='../input/cloud-images-resized/train_images_384x576/', flips=False, augment=False, shrink1=1,
                 shrink2=1, dim=(576,384), clean=False):
        'Initialization'
        self.list_IDs = list_IDs
        self.shuffle = shuffle
        self.batch_size = batch_size
        self.path = path
        self.scale = scale
        self.sub = sub
        self.path = path
        self.width = width
        self.height = height
        self.mode = mode
        self.flips = flips
        self.augment = augment
        self.shrink1 = shrink1
        self.shrink2 = shrink2
        self.dim = dim
        self.clean = clean
        self.on_epoch_end()
        
    def __len__(self):
        'Denotes the number of batches per epoch'
        ct = int(np.floor( len(self.list_IDs) / self.batch_size))
        if len(self.list_IDs)>ct*self.batch_size: ct += 1
        return int(ct)

    def __getitem__(self, index):
        'Generate one batch of data'
        indexes = self.indexes[index*self.batch_size:(index+1)*self.batch_size]
        X, msk = self.__data_generation(indexes)
        if self.augment: X, msk = self.__augment_batch(X, msk)
        if (self.mode=='train_seg')|(self.mode=='validate_seg'): return X, msk
        else: return X

    def on_epoch_end(self):
        'Updates indexes after each epoch'
        self.indexes = np.arange(int( len(self.list_IDs) ))
        if self.shuffle: np.random.shuffle(self.indexes)

    def __data_generation(self, indexes):
        'Generates data containing batch_size samples' 
        # Initialization
        lnn = len(indexes); ex = self.shrink1; ax = self.shrink2
        X = np.empty((lnn,self.height,self.width,3),dtype=np.float32)
        msk = np.empty((lnn,self.height//ax,self.width//ax,4),dtype=np.int8)
        
        # Generate data
        for k in range(lnn):
            img = cv2.imread(self.path + self.list_IDs[indexes[k]]+'.jpg')
            #img = cv2.resize(img,(self.dim[0]//ex,self.dim[1]//ex),interpolation = cv2.INTER_AREA)
            img = img[::ex,::ex,:]
            # AUGMENTATION FLIPS
            hflip = False; vflip = False
            if (self.flips):
                if np.random.uniform(0,1)>0.5: hflip=True
                if np.random.uniform(0,1)>0.5: vflip=True
            if vflip: img = cv2.flip(img,0) # vertical
            if hflip: img = cv2.flip(img,1) # horizontal
            # AUGMENTATION SHAKE
            a = np.random.randint(0,self.dim[0]//ex//ax-self.width//ax+1)
            b = np.random.randint(0,self.dim[1]//ex//ax-self.height//ax+1)
            if (self.mode=='predict'):
                a = (self.dim[0]//ex//ax-self.width//ax)//2
                b = (self.dim[1]//ex//ax-self.height//ax)//2
            img = img[b*ax:self.height+b*ax,a*ax:self.width+a*ax]
            # NORMALIZE IMAGES
            X[k,] = img*self.scale - self.sub      
            # LABELS
            if (self.mode!='predict'):
                for j in range(1,5):
                    rle = train2.loc[self.list_IDs[indexes[k]],'e'+str(j)]
                    if self.clean:
                        if  train2.loc[self.list_IDs[indexes[k]],'o'+str(j)]<0.4:
                            rle = ''
                    mask = rle2maskX(rle,shrink=ex*ax,shape=self.dim)
                    if vflip: mask = np.flip(mask,axis=0)
                    if hflip: mask = np.flip(mask,axis=1)
                    msk[k,:,:,j-1] = mask[b:self.height//ax+b,a:self.width//ax+a]

        return X, msk
    
    def __random_transform(self, img, masks):
        composition = albu.Compose([
            #albu.HorizontalFlip(p=0.5),
            #albu.VerticalFlip(p=0.5),
            albu.ShiftScaleRotate(rotate_limit=30, scale_limit=0.1, p=0.5)
        ])
        
        composed = composition(image=img, mask=masks)
        aug_img = composed['image']
        aug_masks = composed['mask']
        
        return aug_img, aug_masks
    
    def __augment_batch(self, img_batch, masks_batch):
        for i in range(img_batch.shape[0]):
            img_batch[i, ], masks_batch[i, ] = self.__random_transform(
                img_batch[i, ], masks_batch[i, ])
        
        return img_batch, masks_batch
