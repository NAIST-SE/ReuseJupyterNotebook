df = pd.DataFrame({'var':np.arange(300),'CV':np.zeros(300),'diff':np.zeros(300)})
for i in range(300):
    df.loc[i,'CV'] = roc_auc_score(train['target'],train[i])
    df.loc[i,'diff'] = abs(df.loc[i,'CV']-0.5)
print('We need to LB probe',len(df.loc[ df['diff']>0.04 ,'CV']),'variables')
