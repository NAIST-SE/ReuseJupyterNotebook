filters = [256, 128, 64, 32, 16]
REDUCTION = 0; RED = 2**REDUCTION
filters = filters[:5-REDUCTION]

BATCH_SIZE = 16
jaccard_loss = sm.losses.JaccardLoss() 

skf = KFold(n_splits=3, shuffle=True, random_state=RAND)
for k, (idxT0, idxV0) in enumerate( skf.split(train2) ):

    train_idx = train2.index[idxT0]
    val_idx = train2.index[idxV0]

    if k==0: idx_oof_0 = val_idx.copy()
    elif k==1: idx_oof_1 = val_idx.copy()
    elif k==2: idx_oof_2 = val_idx.copy()

    print('#'*20)
    print('### Fold',k,'###')
    print('#'*20)

    if not DO_TRAIN: continue

    train_generator = DataGenerator2(
        train_idx, flips=True, augment=True, shuffle=True, shrink2=RED, batch_size=BATCH_SIZE,
    )

    val_generator = DataGenerator2(
        val_idx, shrink2=RED, batch_size=BATCH_SIZE
    )

    opt = AdamAccumulate(lr=0.001, accum_iters=8)
    model = sm.Unet(
        'efficientnetb2', 
        classes=4,
        encoder_weights='imagenet',
        decoder_filters = filters,
        input_shape=(None, None, 3),
        activation='sigmoid'
    )
    model.compile(optimizer=opt, loss=jaccard_loss, metrics=[dice_coef,kaggle_dice,kaggle_acc])

    checkpoint = ModelCheckpoint('model_'+str(k)+'.h5', save_best_only=True)
    es = EarlyStopping(monitor='val_dice_coef', min_delta=0.001, patience=5, verbose=1, mode='max')
    rlr = ReduceLROnPlateau(monitor='val_dice_coef', factor=0.5, patience=2, verbose=1, mode='max', min_delta=0.001)
    
    history = model.fit_generator(
         train_generator,
         validation_data=val_generator,
         callbacks=[rlr, es, checkpoint],
         epochs=30,
         verbose=2, workers=2
    )
    history_df = pd.DataFrame(history.history)
    history_df.to_csv('history_'+str(k)+'.csv', index=False)

    del train_idx, val_idx, train_generator, val_generator, opt, model, checkpoint, es, rlr, history, history_df
    K.clear_session(); x=gc.collect()
