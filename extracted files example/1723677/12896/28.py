dfPU = pd.DataFrame({'var':np.arange(300),'LB':np.zeros(300)})
for i in range(300):
    logr = LogisticRegression(solver='liblinear').fit(public[[i]],public['target'])
    dfPU.loc[i,'LB'] = roc_auc_score(public['target'],logr.predict_proba(public[[i]])[:,1])
dfPU.sort_values('LB',inplace=True,ascending=False)
dfPU.head()
