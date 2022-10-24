%%time
# FREQUENCY ENCODE 
add_features(X_train,X_test,['uid'],['TransactionDT'],['count'])
# AGGREGATE 
add_features(X_train,X_test,['uid'],['TransactionAmt','D4','D9','D10','D15'],['mean','std'])
# AGGREGATE
add_features(X_train,X_test,['uid'],['C'+str(x) for x in range(1,15) if x!=3],['mean'])
# AGGREGATE
add_features(X_train,X_test,['uid'],['M'+str(x) for x in range(1,10)],['mean'])

# AGGREGATE 
add_features(X_train,X_test,['uid'],['P_emaildomain','dist1','DT_M','id_02','cents'],['nunique'])
# AGGREGATE
add_features(X_train,X_test,['uid'],['C14'],['std'])
# AGGREGATE 
add_features(X_train,X_test,['uid'],['C13','V314'],['nunique'])
# AGGREATE 
add_features(X_train,X_test,['uid'],['V127','V136','V309','V307','V320'],['nunique'])
