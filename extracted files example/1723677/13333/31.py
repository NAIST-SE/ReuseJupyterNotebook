oof = np.empty_like(train2[['e1','e2','e3','e4']].values)

# K-FOLD MODELS
skf = KFold(n_splits=3, shuffle=True, random_state=42)
for k, (idxT, idxV) in enumerate( skf.split(train2) ):
        
    # TRAIN MODEL
    print(); print('#'*10,'FOLD',k,'#'*10)
    print('Train on',len(idxT),'Validate on',len(idxV))
    model = build_model()        
    train_gen = DataGenerator(train2.index[idxT],flips=True, shuffle=True)
    val_gen = DataGenerator(train2.index[idxV])
    h = model.fit_generator(train_gen, epochs = 4, verbose=2, validation_data = val_gen)
        
    # PREDICT OOF
    print('Predict OOF: ',end='')
    oof_gen = DataGenerator(train2.index[idxV], width=1024, height=672, batch_size=2, mode='predict')
    for b,batch in enumerate(oof_gen):
        btc = model.predict_on_batch(batch)
        for j in range(btc.shape[0]):
            for i in range(btc.shape[-1]):
                mask = (btc[j,:,:,i]>0.4).astype(int); rle =''
                if np.sum(mask)>4*20000: rle = mask2rleX( mask )
                oof[idxV[2*b+j],i] = rle
        if b%50==0: print(2*b,', ',end='')
        
    # SAVE MODEL AND FREE GPU MEMORY 
    model.save('Seg_'+str(k)+'.h5', overwrite=True)
    del train_gen, val_gen, oof_gen, model, h, idxT, idxV, btc, batch, b
    K.clear_session(); x=gc.collect()
