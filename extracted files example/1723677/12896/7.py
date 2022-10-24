train = pd.read_csv('../input/train.csv')
df = pd.DataFrame({'var':np.arange(300),'CV':np.zeros(300),'diff':np.zeros(300),'LB':0.5*np.ones(300)})
for i in range(300):
    df.loc[i,'CV'] = roc_auc_score(train['target'],train[str(i)])
    df.loc[i,'diff'] = abs(df.loc[i,'CV']-0.5)
df.sort_values('diff',inplace=True,ascending=False)
df.head()
