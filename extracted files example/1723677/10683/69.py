epochs=10
batch=256
for k in range(epochs):
    # SPLIT TRAINING DATA IN HALF TO FIT INTO GPU MEMORY
    model.fit( [X_train1[col] for col in OHE] + [X_train1[NUM]],Y_train1,
        batch_size=batch, epochs = 1, verbose=2, callbacks=[ #annealer, 
        printAUC(X_train1, Y_train1, OHE, NUM, X_val1, Y_val1, 0, k)],
        validation_data = ([X_val1[col] for col in OHE] + [X_val1[NUM]],Y_val1) )
    model.fit( [X_train2[col] for col in OHE] + [X_train2[NUM]],Y_train2,
        batch_size=batch, epochs = 1, verbose=2, callbacks=[ #annealer, 
        printAUC(X_train2, Y_train2, OHE, NUM, X_val2, Y_val2, 0, k)],
        validation_data = ([X_val2[col] for col in OHE] + [X_val2[NUM]],Y_val2) )
    # SHUFFLE TRAIN
    X_train1['HasDetections'] = Y_train1
    X_train1 = X_train1.sample(frac=1)
    Y_train1 = X_train1['HasDetections']
    del X_train1['HasDetections']
    X_train2['HasDetections'] = Y_train2
    X_train2 = X_train2.sample(frac=1)
    Y_train2 = X_train2['HasDetections']
    del X_train2['HasDetections']
    x=gc.collect()
