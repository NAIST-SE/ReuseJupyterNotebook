train['LowFVC'] = train.FVC.lt(train.FVC.mean()).astype(int)
train.LowFVC.value_counts()
