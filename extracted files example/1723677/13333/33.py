# LOAD CLASSIFICATION PREDICTIONS FROM PREVIOUS KERNEL
# https://www.kaggle.com/cdeotte/cloud-bounding-boxes-cv-0-58
for k in range(1,5): train2['o'+str(k)] = 0
train2[['o1','o2','o3','o4']] = np.load('../input/cloudpred1/oof.npy')[:len(train2),]

# LOAD OOF SEGMENTATION PREDICTIONS FROM 3-FOLD ABOVE
for k in range(1,5): train2['ee'+str(k)] = ''
train2[['ee1','ee2','ee3','ee4']] = oof
for k in range(1,5): train2['ee'+str(k)] = train2['ee'+str(k)].map(clean)

# COMPUTE KAGGLE DICE
th = [0.5,0.5,0.5,0.5]
for k in range(1,5):
    train2['ss'+str(k)] = train2.apply(lambda x:dice_coef6(x['e'+str(k)],x['o'+str(k)],x['ee'+str(k)],th[k-1]),axis=1)
    dice = np.round( train2['ss'+str(k)].mean(),3 )
    print(types[k-1],': Kaggle Dice =',dice)
dice = np.round( np.mean( train2[['ss1','ss2','ss3','ss4']].values ),3 )
print('Overall : Kaggle Dice =',dice)
