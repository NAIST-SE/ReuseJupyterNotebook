class DataGenerator(keras.utils.Sequence):
    # USES GLOBAL VARIABLE TRAIN2 COLUMNS E1, E2, E3, E4
    'Generates data for Keras'
    def __init__(self, list_IDs, batch_size=8, shuffle=False, width=512, height=352, scale=1/128., sub=1., mode='train_seg',
                 path='../input/understanding_cloud_organization/train_images/', ext='.jpg', flips=False, shrink=2):
        'Initialization'
        self.list_IDs = list_IDs
        self.shuffle = shuffle
        self.batch_size = batch_size
        self.path = path
        self.scale = scale
        self.sub = sub
        self.path = path
        self.ext = ext
        self.width = width
        self.height = height
        self.mode = mode
        self.flips = flips
        self.shrink = shrink
        self.on_epoch_end()
        
    def __len__(self):
        'Denotes the number of batches per epoch'
        ct = int(np.floor( len(self.list_IDs) / self.batch_size))
        if len(self.list_IDs)>ct*self.batch_size: ct += 1
        return int(ct)

    def __getitem__(self, index):
        'Generate one batch of data'
        indexes = self.indexes[index*self.batch_size:(index+1)*self.batch_size]
        X, y, msk, crp = self.__data_generation(indexes)
        if (self.mode=='display'): return X, msk, crp
        elif (self.mode=='train_seg')|(self.mode=='validate_seg'): return X, msk
        elif (self.mode=='train')|(self.mode=='validate'): return X, y
        else: return X

    def on_epoch_end(self):
        'Updates indexes after each epoch'
        self.indexes = np.arange(int( len(self.list_IDs) ))
        if self.shuffle: np.random.shuffle(self.indexes)

    def __data_generation(self, indexes):
        'Generates data containing batch_size samples' 
        # Initialization
        lnn = len(indexes)
        X = np.empty((lnn,self.height,self.width,3),dtype=np.float32)
        msk = np.empty((lnn,self.height,self.width,4),dtype=np.int8)
        crp = np.zeros((lnn,2),dtype=np.int16)
        y = np.zeros((lnn,4),dtype=np.int8)
        
        # Generate data
        for k in range(lnn):
            img = cv2.imread(self.path + self.list_IDs[indexes[k]] + self.ext)
            img = cv2.resize(img,(2100//self.shrink,1400//self.shrink),interpolation = cv2.INTER_AREA)
            # AUGMENTATION FLIPS
            hflip = False; vflip = False
            if (self.flips):
                if np.random.uniform(0,1)>0.5: hflip=True
                if np.random.uniform(0,1)>0.5: vflip=True
            if vflip: img = cv2.flip(img,0) # vertical
            if hflip: img = cv2.flip(img,1) # horizontal
            # RANDOM CROP
            a = np.random.randint(0,2100//self.shrink-self.width+1)
            b = np.random.randint(0,1400//self.shrink-self.height+1)
            if (self.mode=='predict'):
                a = (2100//self.shrink-self.width)//2
                b = (1400//self.shrink-self.height)//2
            img = img[b:self.height+b,a:self.width+a]
            # NORMALIZE IMAGES
            X[k,] = img*self.scale - self.sub      
            # LABELS
            if (self.mode!='predict'):
                for j in range(1,5):
                    rle = train2.loc[self.list_IDs[indexes[k]],'e'+str(j)]
                    mask = rle2maskX(rle,shrink=self.shrink)
                    if vflip: mask = np.flip(mask,axis=0)
                    if hflip: mask = np.flip(mask,axis=1)
                    msk[k,:,:,j-1] = mask[b:self.height+b,a:self.width+a]
                    if (self.mode=='train')|(self.mode=='validate'):
                        if np.sum( msk[k,:,:,j-1] )>0: y[k,j-1]=1
            if (self.mode=='display'):
                crp[k,0] = a; crp[k,1] = b

        return X, y, msk, crp
