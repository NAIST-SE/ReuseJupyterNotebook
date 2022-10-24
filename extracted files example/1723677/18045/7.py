%%time

KNN = 100
batch = 1000

test_pred = np.zeros((test.shape[0]),dtype=np.int8)
for g in [0,1,2,3,4]:
    print('Infering group %i'%g)
    
    # TRAIN DATA
    data = train.loc[train.group==g]
    X_train = np.zeros((len(data)-6,7))
    X_train[:,0] = 0.25*data.signal[:-6]
    X_train[:,1] = 0.5*data.signal[1:-5]
    X_train[:,2] = 1.0*data.signal[2:-4]
    X_train[:,3] = 4.0*data.signal[3:-3]
    X_train[:,4] = 1.0*data.signal[4:-2]
    X_train[:,5] = 0.5*data.signal[5:-1]
    X_train[:,6] = 0.25*data.signal[6:]
    y_train = data.open_channels[3:].values

    # TEST DATA
    data = test.loc[test.group==g]
    X_test = np.zeros((len(data)-6,7))
    X_test[:,0] = 0.25*data.signal[:-6]
    X_test[:,1] = 0.5*data.signal[1:-5]
    X_test[:,2] = 1.0*data.signal[2:-4]
    X_test[:,3] = 4.0*data.signal[3:-3]
    X_test[:,4] = 1.0*data.signal[4:-2]
    X_test[:,5] = 0.5*data.signal[5:-1]
    X_test[:,6] = 0.25*data.signal[6:]

    # HERE IS THE CORRECT WAY TO USE CUML KNN 
    #model = KNeighborsClassifier(n_neighbors=KNN)
    #model.fit(X_train,y_train)
    #y_hat = model.predict(X_test)
    #test_pred[test.group==g][1:-1] = y_hat
    #continue
    
    # WE DO THIS BECAUSE CUML v0.12.0 HAS A BUG
    model = NearestNeighbors(n_neighbors=KNN)
    model.fit(X_train)
    distances, indices = model.kneighbors(X_test)

    # FIND PREDICTIONS OURSELVES WITH STATS.MODE
    ct = indices.shape[0]
    pred = np.zeros((ct+6),dtype=np.int8)
    it = ct//batch + int(ct%batch!=0)
    #print('Processing %i batches:'%(it))
    for k in range(it):
        a = batch*k; b = batch*(k+1); b = min(ct,b)
        pred[a+3:b+3] = np.median( y_train[ indices[a:b].astype(int) ], axis=1)
        #print(k,', ',end='')
    #print()
    test_pred[test.group==g] = pred
