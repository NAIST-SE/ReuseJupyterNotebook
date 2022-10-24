types = ['Fish','Flower','Gravel','Sugar']
train_batch = DataGenerator(train2.index[:8], mode='display',batch_size=1,scale=1,sub=0)
for k,image in enumerate(train_batch):
    plt.figure(figsize=(15,8))
    
    # RANDOMLY PICK CLOUD TYPE TO DISPLAY FROM NON-EMPTY MASKS
    idx = np.argwhere( train2.loc[train2.index[k],['d1','d2','d3','d4']].values==1 ).flatten()
    d = np.random.choice(idx)+1
    
    # DISPLAY ORIGINAL
    img = Image.open(PATH+train2.index[k]+'.jpg'); img=np.array(img)
    mask = rle2maskX( train2.loc[train2.index[k],'e'+str(d)] )
    contour = mask2contour( mask,10 )
    img[contour==1,:2]=255
    diff = np.ones((1400,2100,3),dtype=np.int)*255-img.astype(int)
    img=img.astype(int); img[mask==1,:] += diff[mask==1,:]//6
    mask = np.zeros((1400,2100))
    a = image[2][0,1]*2
    b = image[2][0,0]*2
    mask[a:a+2*352,b:b+2*512]=1
    mask = mask2contour(mask,20)
    img[mask==1,:]=0
    plt.subplot(1,2,1); 
    plt.title('Original - '+train2.index[k]+'.jpg - '+types[d-1])
    plt.imshow(img);
    
    # DISPLAY RANDOM CROP
    img = image[0][0,]
    mask = image[1][0,:,:,d-1]
    contour = mask2contour( mask )
    img[contour==1,:2]=255
    diff = np.ones((352,512,3),dtype=np.int)*255-img.astype(int)
    img=img.astype(int); img[mask==1,:] += diff[mask==1,:]//6
    plt.subplot(1,2,2)
    plt.title('Training Crop - '+train2.index[k]+'.jpg - '+types[d-1])
    plt.imshow( img.astype(int) ); 
    plt.show()
