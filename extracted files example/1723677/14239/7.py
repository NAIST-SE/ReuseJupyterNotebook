# PREPARE DATA AND STANDARDIZE
y = train.target
ids = train.id.values
train = train.drop(['id', 'target'], axis=1)
test_ids = test.id.values
test = test[train.columns]

all_auc_NN = []
oof_preds_NN = np.zeros((len(train)))
test_preds_NN = np.zeros((len(test)))

scl = preprocessing.StandardScaler()
scl.fit(pd.concat([train, test]))
train = scl.transform(train)
test = scl.transform(test)
