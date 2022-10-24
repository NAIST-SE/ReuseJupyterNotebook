if TRAIN_MODELS:
    oof = np.zeros((train2.shape[0],4))
    preds = np.zeros((sub.Image.values[::4].shape[0],4))

    skf = KFold(n_splits=3, shuffle=True, random_state=42)
    for k, (idxT, idxV) in enumerate( skf.split(train2) ):

        model = build_model()
        train_gen = DataGenerator(train2.index[idxT],shake=32,flips=True,shuffle=True)
        val_gen = DataGenerator(train2.index[idxV],shake=32,mode='validate')
    
        print()
        print('#'*10,'FOLD',k,'#'*10)
        print('#'*10,'TRAIN','#'*10)
        h = model.fit_generator(train_gen, epochs = 3, verbose=1, validation_data = val_gen)
   
        print('#'*10,'PREDICT','#'*10)
        test_gen = DataGenerator(sub.Image.values[::4], mode='predict', batch_size=8,
                path='../input/understanding_cloud_organization/test_images/', shake=32)
        preds += model.predict_generator(test_gen, verbose=1)
        oof[idxV,] = model.predict_generator(val_gen, verbose=1)
        
        # FREE GPU MEMORY (BEING EXTRA CAREFUL HERE)
        del train_gen, val_gen, test_gen, model, h, idxT, idxV
        K.clear_session(); x=gc.collect()
            
    preds /= skf.n_splits
else:
    oof = np.load('../input/cloudpred1/oof.npy')
    preds = np.load('../input/cloudpred1/preds.npy')
    print('Saving time by loading classification OOF and Preds')
