# FIND STANDARD DEVIATION OF ALL 512*256 BLOCKS
useful = np.zeros((256,512))
for i in range(512):
    partial = train[ train['wheezy-copper-turtle-magic']==i ]
    useful[:,i] = np.std(partial.iloc[:,1:-1], axis=0)
# CONVERT TO BOOLEANS IDENTIFYING USEFULNESS
useful = useful > 1.5
