train = pd.read_csv('../input/train.csv').fillna(' ')

trainX = train['comment_text']
target = train.sum(axis=1).values

sss = StratifiedShuffleSplit(n_splits=5, train_size=0.10)
for train_index, test_index in sss.split(trainX, target):
    train_text = trainX.iloc[train_index] 
    train_tgt = target[train_index]
