startTime = datetime.now()


BASE_DIR = '../input/instant-gratification/'
RANDOM_STATE = 529
MODEL_NUMBER = 'M003'

train = pd.read_csv('{}train.csv'.format(BASE_DIR))
test = pd.read_csv('{}test.csv'.format(BASE_DIR))

oof_qda = np.zeros(len(train))
pred_te_qda = np.zeros(len(test))

cols = [c for c in train.columns if c not in ['id', 'target', 'wheezy-copper-turtle-magic']]

#qda_dict = {}

for i in tqdm(range(512)):
    train2 = train[train['wheezy-copper-turtle-magic']==i]
    test2 = test[test['wheezy-copper-turtle-magic']==i]
    idx1 = train2.index; idx2 = test2.index
    train2.reset_index(drop=True,inplace=True)

    data = pd.concat([pd.DataFrame(train2[cols]), pd.DataFrame(test2[cols])])
    data2 = StandardScaler().fit_transform(PCA(svd_solver='full',n_components='mle').fit_transform(data[cols]))
    train3 = data2[:train2.shape[0]]; test3 = data2[train2.shape[0]:]

    data2 = StandardScaler().fit_transform(VarianceThreshold(threshold=1.5).fit_transform(data[cols]))
    train4 = data2[:train2.shape[0]]; test4 = data2[train2.shape[0]:]

    # STRATIFIED K FOLD (Using splits=25 scores 0.002 better but is slower)
    # qda_dict[i] = {}
    fold = 0
    skf = StratifiedKFold(n_splits=5, random_state=RANDOM_STATE)
    for train_index, test_index in skf.split(train2, train2['target']):
        # clf = QuadraticDiscriminantAnalysis(reg_param=0.111)
        # clf.fit(train4[train_index,:],train2.loc[train_index]['target'])
        clf = qda_dict[i][fold]
        oof_qda[idx1[test_index]] = clf.predict_proba(train4[test_index,:])[:,1]
        pred_te_qda[idx2] += clf.predict_proba(test4)[:,1] / skf.n_splits
        # qda_dict[i][fold] = clf
        fold += 1

CV_SCORE = roc_auc_score(train['target'], oof_qda)
print('qda', roc_auc_score(train['target'], oof_qda))
