train = pd.read_csv('../input/train.csv')
test = pd.read_csv('../input/test.csv')

train_T = train.T.drop(['ID_code','target'])
train_T['feat_mean'] = train_T.mean(axis=1)

train_T['feat_max'] = train_T[[x for x in range(0,200000)]].max(axis=1)
train_T['feat_min'] = train_T[[x for x in range(0,200000)]].min(axis=1)
train_T['feat_std'] = train_T[[x for x in range(0,200000)]].std(axis=1)
train_T['feat_var'] = train_T[[x for x in range(0,200000)]].var(axis=1)
train_T['feat_range'] = train_T['feat_max'] - train_T['feat_min']
