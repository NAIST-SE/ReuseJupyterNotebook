sub.loc[ sub['target']>1 , 'target'] = 1
b = plt.hist(sub['target'], bins=200)
