# ADD UID FEATURE
X_train['day'] = X_train.TransactionDT / (24*60*60)
X_train['uid'] = X_train.card1_addr1.astype(str)+'_'+(X_train.day-X_train.D1).floor().astype(str)

X_test['day'] = X_test.TransactionDT / (24*60*60)
X_test['uid'] = X_test.card1_addr1.astype(str)+'_'+(X_test.day-X_test.D1).floor().astype(str)
# LABEL ENCODE
encode_LE(X_train,X_test,'uid',verbose=False)
