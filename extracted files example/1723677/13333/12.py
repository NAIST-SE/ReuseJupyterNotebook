th = [0.65,0.65,0.65,0.65]
for k in range(1,5):
    train2['ss'+str(k)] = train2.apply(lambda x:dice_coef6(x['e'+str(k)],x['o'+str(k)],x['bb'+str(k)],th[k-1]),axis=1)
    dice = np.round( train2['ss'+str(k)].mean(),3 )
    print(type[k-1],': Kaggle Dice =',dice)
dice = np.round( np.mean( train2[['ss1','ss2','ss3','ss4']].values ),3 )
print('Overall : Kaggle Dice =',dice)
