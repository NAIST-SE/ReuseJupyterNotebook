NFOLDS = 15
RANDOM_STATE = 42

gc.collect()
# STRATIFIED K FOLD
folds = StratifiedKFold(n_splits=NFOLDS, shuffle=True, random_state=RANDOM_STATE)
for fold_, (trn_, val_) in enumerate(folds.split(y, y)):
    #print("Current Fold: {}".format(fold_))
    trn_x, trn_y = train[trn_, :], y.iloc[trn_]
    val_x, val_y = train[val_, :], y.iloc[val_]

    # BUILD MODEL
    inp = Input(shape=(trn_x.shape[1],))
    x = Dense(2000, activation="relu")(inp)
    x = BatchNormalization()(x)
    x = Dropout(0.3)(x)
    x = Dense(1000, activation="relu")(x)
    x = BatchNormalization()(x)
    x = Dropout(0.3)(x)
    x = Dense(500, activation="relu")(x)
    x = BatchNormalization()(x)
    x = Dropout(0.2)(x)
    x = Dense(100, activation="relu")(x)
    x = BatchNormalization()(x)
    x = Dropout(0.2)(x)
    out = Dense(1, activation="sigmoid")(x)
    clf = Model(inputs=inp, outputs=out)
    clf.compile(loss='binary_crossentropy', optimizer="adam", metrics=[auc])
    
    # CALLBACKS
    es = callbacks.EarlyStopping(monitor='val_auc', min_delta=0.001, patience=10,
                verbose=0, mode='max', baseline=None, restore_best_weights=True)
    rlr = callbacks.ReduceLROnPlateau(monitor='val_auc', factor=0.5,
                patience=3, min_lr=1e-6, mode='max', verbose=0)

    # TRAIN
    clf.fit(trn_x, trn_y, validation_data=(val_x, val_y), callbacks=[es, rlr], epochs=100, 
                batch_size=1024, verbose=0)
    
    # PREDICT TEST
    test_fold_preds = clf.predict(test)
    test_preds_NN += test_fold_preds.ravel() / NFOLDS
    
    # PREDICT OOF
    val_preds = clf.predict(val_x)
    oof_preds_NN[val_] = val_preds.ravel()
    
    # RECORD AUC
    val_auc = round( metrics.roc_auc_score(val_y, val_preds),5 )
    all_auc_NN.append(val_auc)
    print('Fold',fold_,'has AUC =',val_auc)
    
    K.clear_session()
    gc.collect()
