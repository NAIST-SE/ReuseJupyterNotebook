for d in range(1,5):
    print('#'*27); print('#'*5,types[d-1].upper(),'CLOUDS','#'*7); print('#'*27)
    plt.figure(figsize=(20,15)); k=0
    for kk in range(9):
        plt.subplot(3,3,kk+1)
        while (train2.loc[train2.index[k],'e'+str(d)]==''): k += 1
        f = train2.index[k]+'.jpg'
        img = Image.open(PATH+f); img = img.resize((525,350)); img = np.array(img)
        rle1 = train2.loc[train2.index[k],'e'+str(d)]; mask = rle2maskX(rle1,shrink=4)
        contour = mask2contour(mask,5); img[contour==1,:2] = 255
        rle2 = train2.loc[train2.index[k],'ee'+str(d)]; mask = rle2maskX(rle2,shape=(525,350))
        contour = mask2contour(mask,5); img[contour==1,2] = 255
        diff = np.ones((350,525,3),dtype=np.int)*255-img
        img=img.astype(int); img[mask==1,:] += diff[mask==1,:]//4
        dice = np.round( dice_coef6(rle1,1,rle2,0),3 )
        plt.title(f+'  Dice = '+str(dice)+'   Yellow true, Blue predicted')
        plt.imshow(img); k += 1
    plt.show()
