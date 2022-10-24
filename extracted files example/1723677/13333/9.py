type2 = ['FISH','FLOWER','GRAVEL','SUGAR']
if TRAIN_MODELS:
    oof_bb = np.zeros((train2.shape[0],4,4))
    preds_bb = np.zeros((sub.Image.values[::4].shape[0],4,4))

    skf = KFold(n_splits=3, shuffle=True, random_state=42)
    for k, (idxT, idxV) in enumerate( skf.split(train2) ):
        print(); print('#'*28)
        print('#'*10,'FOLD',k,'#'*10)
        print('#'*28)
        for j in [1,2,3,4]:
            model = build_model()
            one = train2[ (train2.index.isin(train2.index[idxT]))&(train2['d'+str(j)]==1)&(train2['s'+str(j)]>0.8)&(train2['o'+str(j)]>0.5) ]
            two = train2[ (train2.index.isin(train2.index[idxV]))&(train2['d'+str(j)]==1)&(train2['s'+str(j)]>0.8)&(train2['o'+str(j)]>0.5) ]
            train_gen = DataGenerator(one.index,mode='train_bb',shuffle=True,flips=True,dft=j)
            val_gen = DataGenerator(two.index,mode='train_bb',dft=j)
        
            print(); print('#'*10,'TRAIN CLOUD',type2[j-1],' (fold',str(k)+')','#'*10)
            print(' train on',len(one),', validate on',len(two))
            h = model.fit_generator(train_gen, epochs = 5, verbose=1, validation_data = val_gen)

    
            print('#'*10,'PREDICT OOF AND TEST','#'*10)
            test_gen = DataGenerator(sub.Image.values[::4], mode='predict', batch_size=8,
                    path='test_images/')
            val_gen2 = DataGenerator(train2.index[idxV],mode='predict')
            preds_bb[:,:,j-1] += model.predict_generator(test_gen, verbose=1)
            oof_bb[idxV,:,j-1] = model.predict_generator(val_gen2, verbose=1)
        
            # FREE GPU MEMORY
            del train_gen, val_gen, val_gen2, test_gen, model, h, annealer, one, two
            K.clear_session(); x=gc.collect()
            
    preds_bb /= skf.n_splits
else:
    oof_bb = np.load('../input/cloudpred1/oof_bb.npy')
    preds_bb = np.load('../input/cloudpred1/preds_bb.npy')
    print('Saving time by loading Bounding Box OOF and Preds')
