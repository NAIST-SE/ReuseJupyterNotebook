# START WITH BEST TRAINING DATA MODEL
clf = LogisticRegression(solver='liblinear',penalty='l1',C=0.1, class_weight='balanced')
clf.fit(train.iloc[:,:-1],train['target']) 
u0 = clf.coef_[0]
u0 = u0 / np.sqrt(u0.dot(u0))

# INITIAL SCORES
aucPU = round(roc_auc_score(public['target'],u0.dot(public.iloc[:,:-1].values.transpose())),5)
aucPR = round(roc_auc_score(private['target'],u0.dot(private.iloc[:,:-1].values.transpose())),5)
bestPU = aucPU; currentPR = aucPR; initial = u0.copy()
print('Our starting model has LB =',aucPU,'and Private score =',aucPR)

# ACCELERATE RANDOM SEARCH BY NEGLECTING 250 LEAST IMPORTANT VARIABLES FROM TRAINING DATA
df = pd.DataFrame({'var':np.arange(300),'CV':np.zeros(300),'diff':np.zeros(300)})
for i in range(300):
    df.loc[i,'CV'] = roc_auc_score(train['target'],train[i])
    df.loc[i,'diff'] = abs(df.loc[i,'CV']-0.5)
df.sort_values('diff',inplace=True,ascending=False)
