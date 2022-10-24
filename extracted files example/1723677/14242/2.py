%%time
# LOAD TRAIN
X_train = cudf.read_csv('../input/ieee-fraud-detection/train_transaction.csv',index_col='TransactionID', usecols=cols+['isFraud'],dtype=dtypes)
train_id = cudf.read_csv('../input/ieee-fraud-detection/train_identity.csv',index_col='TransactionID',dtype=dtypes)
X_train = X_train.merge(train_id, how='left', left_index=True, right_index=True)
# LOAD TEST
X_test = cudf.read_csv('../input/ieee-fraud-detection/test_transaction.csv',index_col='TransactionID', usecols=cols,dtype=dtypes)
test_id = cudf.read_csv('../input/ieee-fraud-detection/test_identity.csv',index_col='TransactionID', dtype=dtypes)
fix = {o:n for o, n in zip(test_id.columns, train_id.columns)}
test_id.rename(columns=fix, inplace=True)
X_test = X_test.merge(test_id, how='left', left_index=True, right_index=True)
# PRINT SHAPE
del train_id, test_id; x = gc.collect()
print('Train shape on GPU',X_train.shape,'Test shape on GPU',X_test.shape)
