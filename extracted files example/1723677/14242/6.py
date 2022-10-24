%%time
# TRANSACTION AMT CENTS
X_train['cents'] = (X_train['TransactionAmt'] - X_train['TransactionAmt'].floor()).astype('float32')
X_test['cents'] = (X_test['TransactionAmt'] - X_test['TransactionAmt'].floor()).astype('float32')
print('cents, ', end='')
# FREQUENCY ENCODE
add_features(X_train,X_test,['addr1','card1','card2','card3','P_emaildomain'],['TransactionDT'],['count'])
# COMBINE COLUMNS 
encode_CB(X_train,X_test,'card1','addr1')
encode_CB(X_train,X_test,'card1_addr1','P_emaildomain')
# FREQUENCY ENCODE
add_features(X_train,X_test,['card1_addr1','card1_addr1_P_emaildomain'],['TransactionDT'],['count'])
# GROUP AGGREGATE
add_features(X_train,X_test,['card1','card1_addr1','card1_addr1_P_emaildomain'],\
    ['TransactionAmt','D9','D11'],['mean','std'])
