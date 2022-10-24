oof = np.zeros(len(public))
rskf = RepeatedStratifiedKFold(n_splits=25, n_repeats=5)
for train_index, test_index in rskf.split(public.iloc[:,:-1], public['target']):
    clf = LogisticRegression(solver='liblinear',penalty='l1',C=0.1,class_weight='balanced')
    clf.fit(public.loc[train_index].iloc[:,:-1],public.loc[train_index]['target'])
    oof[test_index] += clf.predict_proba(public.loc[test_index].iloc[:,:-1])[:,1]
aucPU = round(roc_auc_score(public['target'],oof),5)
print('LB =',aucPU)
