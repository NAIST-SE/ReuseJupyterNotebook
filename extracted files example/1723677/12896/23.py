dfTR = pd.DataFrame({'var':np.arange(300),'CV':np.zeros(300)})
for i in range(300):
    logr = LogisticRegression(solver='liblinear').fit(train[[i]],train['target'])
    dfTR.loc[i,'CV'] = roc_auc_score(train['target'],logr.predict_proba(train[[i]])[:,1])
dfTR.sort_values('CV',inplace=True,ascending=False)
dfTR.head()
