cols = list( X_train.columns )
# REMOVE FEATURES
cols.remove('TransactionDT'); cols.remove('isFraud')
for c in ['D6','D7','D8','D9','D12','D13','D14'] + ['DT_M','day','uid']:
    cols.remove(c)  
# FAILED TIME CONSISTENCY TEST
for c in ['C3','M5','id_08','id_33']:
    cols.remove(c)
for c in ['card4','id_07','id_14','id_21','id_30','id_32','id_34']:
    cols.remove(c)
for c in ['id_'+str(x) for x in range(22,28)]:
    cols.remove(c)
