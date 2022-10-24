print('Computing masks for',len(sub)//4,'test images with 3 models'); sub.EncodedPixels = ''
PTH = '../input/understanding_cloud_organization/test_images/'
test_gen = DataGenerator(sub.Image[::4].values, width=1024, height=672, batch_size=2, mode='predict',path=PTH)

for b,batch in enumerate(test_gen):
    btc = model1.predict_on_batch(batch)
    btc += model2.predict_on_batch(batch)
    btc += model3.predict_on_batch(batch)
    btc /= 3.0
    for j in range(btc.shape[0]):
        for i in range(btc.shape[-1]):
            mask = (btc[j,:,:,i]>0.4).astype(int); rle = ''
            if np.sum(mask)>4*20000: rle = mask2rleX( mask )
            sub.iloc[4*(2*b+j)+i,1] = rle
    if b%50==0: print(b*2,', ',end='')
