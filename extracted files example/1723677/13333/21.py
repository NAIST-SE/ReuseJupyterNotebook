# NEW MODEL FROM OLD TO EXTRACT ACTIVATION MAPS
all_layer_weights = model.layers[-1].get_weights()[0]
cam_model = Model(inputs=model.input, 
        outputs=(model.layers[-3].output, model.layers[-1].output)) 

# DISPLAY 25 RANDOM IMAGES
PATH = '../input/understanding_cloud_organization/train_images/'
IMGS = os.listdir(PATH)
for k in np.random.randint(0,5000,25):
    
    # LOAD IMAGE AND PREDICT CLASS ACTIVATION MAP
    img = cv2.resize( cv2.imread(PATH+IMGS[k]), (512, 352))
    x = np.expand_dims(img, axis=0)/128. -1.
    last_conv_output, pred_vec = cam_model.predict(x) 
    last_conv_output = np.squeeze(last_conv_output) 
    pred = np.argmax(pred_vec)
    layer_weights = all_layer_weights[:, pred] 
    final_output = np.dot(last_conv_output.reshape((16*11, 2048)), layer_weights).reshape(11,16) 
    final_output = scipy.ndimage.zoom(final_output, (32, 32), order=1) 

    # DISPLAY IMAGE WITH CLASS ACTIVATION MAPS
    plt.figure(figsize=(12,6))
    plt.subplot(1,2,1)
    mx = np.round( np.max(final_output),1 )
    mn = np.round( np.min(final_output),1 )
    final_output = (final_output-mn)/(mx-mn)
    mask0 = (final_output>0.3).astype(int)
    contour0 = mask2contour(mask0,5)
    plt.imshow(img, alpha=0.5)
    plt.imshow(final_output, cmap='jet', alpha=0.5)
    plt.title('Found '+types[pred]+'  -  Pr = '+str(np.round(pred_vec[0,pred],3)) )
    
    # DISPLAY IMAGE WITH MASKS
    plt.subplot(1,2,2)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    rle = train2.loc[IMGS[k].split('.')[0],'e'+str(pred+1)]
    mask = rle2mask2X(rle,shrink=(512,352))
    contour = mask2contour(mask,5)
    img[contour==1,:2] = 255
    img[contour0==1,2] = 255
    diff = np.ones((352,512,3),dtype=np.int)*255-img
    img=img.astype(int); img[mask0==1,:] += diff[mask0==1,:]//4
    plt.imshow( img )
    dice = np.round( dice_coef8(mask,mask0),3 )
    plt.title('Dice = '+str(dice)+'  -  '+IMGS[k]+'  -  '+types[pred])
    
    plt.show()
