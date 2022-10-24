print('Computing masks for',len(sub)//4,'test images with 3 models'); sub.EncodedPixels = ''
PTH = '../input/cloud-images-resized/test_images_384x576/'; bs = 4
if USE_TTA: bs=1
test_gen = DataGenerator2(sub.Image[::4].values, width=576, height=384, batch_size=bs, mode='predict',path=PTH)

sz = 20000.*(576/525)*(384/350)/RED/RED

pixt = [0.5,0.5,0.5,0.35] #; pixt = [0.4,0.4,0.4,0.4]
szt = [25000., 20000., 22500., 15000.] #; szt = [20000., 20000., 20000., 20000.]
for k in range(len(szt)): szt[k] = szt[k]*(576./525.)*(384./350.)/RED/RED

if DO_TEST:
    for b,batch in enumerate(test_gen):
        btc = model1.predict_on_batch(batch)
        btc += model2.predict_on_batch(batch)
        btc += model3.predict_on_batch(batch)
        btc /= 3.0

        for j in range(btc.shape[0]):
            for i in range(btc.shape[-1]):
                mask = (btc[j,:,:,i]>pixt[i]).astype(int); rle = ''
                if np.sum(mask)>szt[i]: rle = mask2rleXXX( mask ,shape=(576//RED,384//RED))
                sub.iloc[4*(bs*b+j)+i,1] = rle
        if b%(100//bs)==0: print(b*bs,', ',end='')
        t = np.round( (time.time() - kernel_start)/60,1 )
        if t > LIMIT*60:
            print('#### EXCEEDED TIME LIMIT. STOPPING NOW ####')
            break

    sub[['Image_Label','EncodedPixels']].to_csv('sub_seg.csv',index=False)
    sub.loc[(sub.p<0.5)&(sub.Label=='Fish'),'EncodedPixels'] = ''
    sub.loc[(sub.p<0.3)&(sub.Label=='Flower'),'EncodedPixels'] = ''
    sub.loc[(sub.p<0.5)&(sub.Label=='Gravel'),'EncodedPixels'] = ''
    sub.loc[(sub.p<0.5)&(sub.Label=='Sugar'),'EncodedPixels'] = ''
    sub[['Image_Label','EncodedPixels']].to_csv('submission.csv',index=False)

sub.head(10)
