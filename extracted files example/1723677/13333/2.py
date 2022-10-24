class DataGenerator(keras.utils.Sequence):
    # USES GLOBAL VARIABLE TRAIN2 COLUMNS E1, E2, E3, E4
    'Generates data for Keras'
    def __init__(self, list_IDs, batch_size=8, shuffle=False, width=525, height=350, scale=1/128., sub=1., mode='train',
                 path='../input/understanding_cloud_organization/train_images/', ext='.jpg', shake=0, flips=False, dft=1):
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
        self.shake = shake
        self.flips = flips
        self.dft = dft
        self.on_epoch_end()
        if (mode=='train_bb')&((width!=525)|(height!=350)|(shake>0)):
            print('ERROR: wrong size or shake for train_bb')
        
    def __len__(self):
        'Denotes the number of batches per epoch'
        ct = int(np.floor( len(self.list_IDs) / self.batch_size))
        if len(self.list_IDs)>ct*self.batch_size: ct += 1
        return int(ct)

    def __getitem__(self, index):
        'Generate one batch of data'
        indexes = self.indexes[index*self.batch_size:(index+1)*self.batch_size]
        X, y, bb = self.__data_generation(indexes)
        if (self.mode=='train')|(self.mode=='validate'): return X, y
        elif self.mode=='train_bb': return X, bb
        else: return X

    def on_epoch_end(self):
        'Updates indexes after each epoch'
        self.indexes = np.arange(int( len(self.list_IDs) ))
        if self.shuffle: np.random.shuffle(self.indexes)

    def __data_generation(self, indexes):
        'Generates data containing batch_size samples' 
        # Initialization
        lnn = len(indexes)
        X = np.empty((lnn,self.height-self.shake,self.width-self.shake,3),dtype=np.float32)
        y = np.zeros((lnn,4),dtype=np.int8)
        bb = np.zeros((lnn,4),dtype=np.int16)
        
        # Generate data
        for k in range(lnn):
            img = cv2.imread(self.path + self.list_IDs[indexes[k]] + self.ext)
            img = cv2.resize(img,(self.width,self.height),interpolation = cv2.INTER_AREA)
            # AUGMENTATION FLIPS
            hflip = False; vflip = False
            if (self.flips):
                if np.random.uniform(0,1)>0.5: hflip=True
                if np.random.uniform(0,1)>0.5: vflip=True
            if vflip: img = cv2.flip(img,0) # vertical
            if hflip: img = cv2.flip(img,1) # horizontal
            # AUGMENTATION SHAKE
            a = 0; b = 0
            if self.shake>0:
                a = np.random.randint(0,self.shake+1)
                b = np.random.randint(0,self.shake+1)
                if (self.mode=='predict')|(self.mode=='validate'):
                    a = self.shake//2; b = self.shake//2
            img = img[b:(self.height-self.shake)+b,a:(self.width-self.shake)+a]
            # NORMALIZE IMAGES
            X[k,] = img*self.scale - self.sub      
            # LABELS
            if (self.mode=='train')|(self.mode=='validate'):
                y[k,] = train2.loc[self.list_IDs[indexes[k]],['d1','d2','d3','d4']].values
            # BOUNDING BOXES
            if (self.mode=='train_bb'):
                bb[k,] = train2.loc[self.list_IDs[indexes[k]],'b'+str(self.dft)]
                bb[k,] = bb[k,]//4
                if vflip: bb[k,0] = (350-bb[k,0])-bb[k,2]
                if hflip: bb[k,1] = (525-bb[k,1])-bb[k,3]
            
        return X, y, bb
