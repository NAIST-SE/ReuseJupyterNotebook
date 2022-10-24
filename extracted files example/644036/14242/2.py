FEATURES = [f for f in train_transaction.columns if f not in ['TransactionID','isFraud','TransactionDT']]
CAT_FEATS = train_transaction.select_dtypes('object').columns
# Fill NA Categorical Features
train_transaction[CAT_FEATS] = train_transaction[CAT_FEATS].fillna('_NA_')
test_transaction[CAT_FEATS] = test_transaction[CAT_FEATS].fillna('_NA_')
X = train_transaction[FEATURES]
y = train_transaction['isFraud']
X_test = test_transaction[FEATURES]
