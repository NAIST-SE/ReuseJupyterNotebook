oof = np.zeros(len(train))
predsPU= np.zeros(len(public))
predsPR= np.zeros(len(private))
rskf = RepeatedStratifiedKFold(n_splits=25, n_repeats=5)
for train_index, test_index in rskf.split(train.iloc[:,:-1], train['target']):
    clf = LogisticRegression(solver='liblinear',penalty='l1',C=0.1,class_weight='balanced')
    clf.fit(train.loc[train_index].iloc[:,:-1],train.loc[train_index]['target'])
    oof[test_index] += clf.predict_proba(train.loc[test_index].iloc[:,:-1])[:,1]
    predsPU += clf.predict_proba(public.iloc[:,:-1])[:,1]
    predsPR += clf.predict_proba(private.iloc[:,:-1])[:,1]
aucTR = round(roc_auc_score(train['target'],oof),5)
aucPU = round(roc_auc_score(public['target'],predsPU),5)
aucPR = round(roc_auc_score(private['target'],predsPR),5)
print('LR Model with L1-penalty: CV =',aucTR,'LB =',aucPU,'Private score =',aucPR)
