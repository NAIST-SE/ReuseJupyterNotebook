# DETERMINE TRAIN DATASET STRUCTURE
useful_train = np.zeros((256,512))
for i in range(512):
    partial = train[ train['wheezy-copper-turtle-magic']==i ]
    useful_train[:,i] = np.std(partial.iloc[:,1:-1], axis=0)
useful_train = useful_train > 1.5

# DETERMINE PUBLIC TEST DATASET STRUCTURE
useful_public = np.zeros((256,512))
for i in range(512):
    partial = public[ public['wheezy-copper-turtle-magic']==i ]
    useful_public[:,i] = np.std(partial.iloc[:,1:], axis=0)
useful_public = useful_public > 1.5

# DETERMINE PRIVATE TEST DATASET STRUCTURE
useful_private = np.zeros((256,512))
for i in range(512):
    partial = private[ private['wheezy-copper-turtle-magic']==i ]
    useful_private[:,i] = np.std(partial.iloc[:,1:], axis=0)
useful_private = useful_private > 1.5
