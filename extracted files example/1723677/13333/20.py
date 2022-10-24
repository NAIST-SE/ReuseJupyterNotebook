# PREDICT HOLDOUT SET
train3 = train2.loc[train2.index.isin(idxV)].copy()
oof_gen = DataGenerator(train3.index.values, mode='predict')
oof = model.predict_generator(oof_gen, verbose=2)
for k in range(1,5): train3['o'+str(k)] = 0
train3[['o1','o2','o3','o4']] = oof

# COMPUTE ACCURACY AND ROC_AUC_SCORE
types = ['Fish','Flower','Gravel','Sugar']
for k in range(1,5):
    print(types[k-1],': ',end='')
    auc = np.round( roc_auc_score(train3['d'+str(k)].values,train3['o'+str(k)].values  ),3 )
    acc = np.round( accuracy_score(train3['d'+str(k)].values,(train3['o'+str(k)].values>0.5).astype(int) ),3 )
    print('AUC =',auc,end='')
    print(', ACC =',acc) 
print('OVERALL: ',end='')
auc = np.round( roc_auc_score(train3[['d1','d2','d3','d4']].values.reshape((-1)),train3[['o1','o2','o3','o4']].values.reshape((-1)) ),3 )
acc = np.round( accuracy_score(train3[['d1','d2','d3','d4']].values.reshape((-1)),(train3[['o1','o2','o3','o4']].values>0.5).astype(int).reshape((-1)) ),3 )
print('AUC =',auc, end='')
print(', ACC =',acc) 
