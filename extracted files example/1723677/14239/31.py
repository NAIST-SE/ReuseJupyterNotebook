# RUN LOCALLY AND VALIDATE
models = 512
RunLocally = True

# RUN SUBMITTED TO KAGGLE
if len(df_test)>512*300: 
    repeat = 1
    models = 512 * repeat
    RunLocally = False
    
# INITIALIZE
all_preds = np.zeros(len(df_test))
all_y_pu = np.array([])
all_y_pr = np.array([])
all_preds_pu = np.array([])
all_preds_pr = np.array([])

# MODEL AND PREDICT
for k in range(models):
    
    # IF RUN LOCALLY AND VALIDATE
    # THEN USE SYNTHETIC DATA
    if RunLocally:
        obs = 512
        X, y = make_classification(n_samples=1024, n_features=useful[k%512], 
                    n_informative=useful[k%512], n_redundant=0, n_repeated=0,
                    n_classes=2, n_clusters_per_class=3, weights=None, flip_y=0.05,
                    class_sep=1.0, hypercube=True, shift=0.0, scale=1.0, shuffle=True,
                    random_state=None)
        
    # IF RUN SUBMITTED TO KAGGLE
    # THEN USE REAL DATA
    else:
        df_train2 = df_train[df_train['wheezy-copper-turtle-magic']==k%512]
        df_test2 = df_test[df_test['wheezy-copper-turtle-magic']==k%512]
        sel = VarianceThreshold(1.5).fit(df_train2.iloc[:,1:-1])
        df_train3 = sel.transform(df_train2.iloc[:,1:-1])
        df_test3 = sel.transform(df_test2.iloc[:,1:])
        obs = df_train3.shape[0]
        X = np.concatenate((df_train3,df_test3),axis=0)
        y = np.concatenate((df_train2['target'].values,np.zeros(len(df_test2))))
    
    # TRAIN AND TEST DATA
    train = X[:obs,:]
    train_y = y[:obs]
    test = X[obs:,:]
    test_y = y[obs:]
    comb = X
                
    # FIRST MODEL : QDA
    clf = QuadraticDiscriminantAnalysis(priors = [0.5,0.5])
    clf.fit(train,train_y)
    test_pred = clf.predict_proba(test)[:,1]
    
    # SECOND MODEL : PSEUDO LABEL + QDA
    test_pred = test_pred > np.random.uniform(0,1,len(test_pred)) #randomness
    clf = QuadraticDiscriminantAnalysis(priors = [0.5, 0.5])
    clf.fit(comb, np.concatenate((train_y,test_pred)) )
    test_pred = clf.predict_proba(test)[:,1]
   
    # THIRD MODEL : PSEUDO LABEL + GAUSSIAN MIXTURE
    test_pred = test_pred > np.random.uniform(0,1,len(test_pred)) #randomness
    all_y = np.concatenate((train_y,test_pred))
    least = 0; ct = 1; thx=150
    while least<thx:
        # STOPPING CRITERIA
        if ct>=10: thx -= 10
        else: thx = 150
        # FIND CLUSTERS 
        clusters = np.zeros((len(comb),6))
        # FIND THREE TARGET=1 CLUSTERS
        train4 = comb[ all_y==1, :]
        clf = GaussianMixture(n_components=3).fit(train4) #randomness
        clusters[ all_y==1, 3:] = clf.predict_proba(train4)
        # FIND THREE TARGET=0 CLUSTERS
        train4 = comb[ all_y==0, :]
        clf = GaussianMixture(n_components=3).fit(train4) #randomness
        clusters[ all_y==0, :3] = clf.predict_proba(train4)
        # ADJUST CLUSTERS (EXPLAINED IN KERNEL COMMENTS)
        for j in range(5): clusters[:,j+1] += clusters[:,j]
        rand = np.random.uniform(0,1,clusters.shape[0])
        for j in range(6): clusters[:,j] = clusters[:,j]>rand #randomness
        clusters2 = 6 - np.sum(clusters,axis=1)
        # IF IMBALANCED TRY AGAIN 
        least = pd.Series(clusters2).value_counts().min(); ct += 1

    # FOURTH MODEL : GAUSSIAN MIXTURE + QDA
    clf = QuadraticDiscriminantAnalysis(priors = [0.167, 0.167, 0.167, 0.167, 0.167, 0.167])
    clf.fit(comb,clusters2)
    pds = clf.predict_proba(test)
    test_pred = pds[:,3]+pds[:,4]+pds[:,5]
        
    # IF RUN LOCALLY, STORE TARGETS AND PREDS
    if RunLocally:
        all_y_pu = np.append(all_y_pu, test_y[:256])
        all_y_pr = np.append(all_y_pr, test_y[256:])
        all_preds_pu = np.append(all_preds_pu, test_pred[:256])
        all_preds_pr = np.append(all_preds_pr, test_pred[256:])
    # IF RUN SUBMIT TO KAGGLE, PREDICT TEST.CSV
    else:
        all_preds[df_test2.index] += test_pred / repeat
        
    # PRINT PROGRESS
    if ((k+1)%64==0)|(k==0): print('modeled and predicted',k+1,'magic sub datasets')

# IF RUN LOCALLY, COMPUTE AND PRINT VALIDATION AUCS
if RunLocally: 
    all_y_pu_pr = np.concatenate((all_y_pu,all_y_pr))
    all_preds_pu_pr = np.concatenate((all_preds_pu,all_preds_pr))
    auc1 = roc_auc_score(all_y_pu_pr, all_preds_pu_pr)
    auc2 = roc_auc_score(all_y_pu, all_preds_pu)
    auc3 = roc_auc_score(all_y_pr, all_preds_pr)
    print()
    print('Validation AUC =',np.round(auc1,5))
    print('Approx Public LB =',np.round(auc2,5))
    print('Approx Private LB =',np.round(auc3,5))
