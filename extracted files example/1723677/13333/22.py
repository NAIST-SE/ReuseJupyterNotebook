print('Computing',len(train3),'masks...')
for i in range(1,5): train3['p'+str(i)] = ''
for i in range(1,5): train3['pp'+str(i)] = 0

for i,f in enumerate(train3.index.values):
    
    # LOAD IMAGE AND PREDICT CLASS ACTIVATION MAPS
    img = cv2.resize( cv2.imread(PATH+f+'.jpg'), (512, 352))
    x = np.expand_dims(img, axis=0)/128. -1.
    last_conv_output, pred_vec = cam_model.predict(x) 
    last_conv_output = np.squeeze(last_conv_output) 
    
    for pred in [0,1,2,3]:
        # CREATE FOUR MASKS FROM ACTIVATION MAPS
        layer_weights = all_layer_weights[:, pred]  
        final_output = np.dot(last_conv_output.reshape((16*11, 2048)), layer_weights).reshape(11,16) 
        final_output = scipy.ndimage.zoom(final_output, (32, 32), order=1)
        mx = np.round( np.max(final_output),1 )
        mn = np.round( np.min(final_output),1 )
        final_output = (final_output-mn)/(mx-mn)
        final_output = cv2.resize(final_output,(525,350))
        train3.loc[f,'p'+str(pred+1)] = mask2rle( (final_output>0.3).astype(int) )
        train3.loc[f,'pp'+str(pred+1)] = pred_vec[0,pred]
    if i%25==0: print(i,', ',end='')
print(); print()
        
# COMPUTE KAGGLE DICE
th = [0.8,0.5,0.7,0.7]
for k in range(1,5):
    train3['ss'+str(k)] = train3.apply(lambda x:dice_coef6(x['e'+str(k)],x['p'+str(k)],x['pp'+str(k)],th[k-1]),axis=1)
    dice = np.round( train3['ss'+str(k)].mean(),3 )
    print(types[k-1],': Kaggle Dice =',dice)
dice = np.round( np.mean( train3[['ss1','ss2','ss3','ss4']].values ),3 )
print('Overall : Kaggle Dice =',dice)
