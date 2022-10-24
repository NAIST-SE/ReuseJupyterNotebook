type = ['Fish','Flower','Gravel','Sugar']
for k in range(1,5): train2['o'+str(k)] = 0
train2[['o1','o2','o3','o4']] = oof

for k in range(1,5):
    print(type[k-1],': ',end='')
    auc = np.round( roc_auc_score(train2['d'+str(k)].values,train2['o'+str(k)].values  ),3 )
    acc = np.round( accuracy_score(train2['d'+str(k)].values,(train2['o'+str(k)].values>0.5).astype(int) ),3 )
    print('AUC =',auc,end='')
    print(', ACC =',acc) 
print('OVERALL: ',end='')
auc = np.round( roc_auc_score(train2[['d1','d2','d3','d4']].values.reshape((-1)),train2[['o1','o2','o3','o4']].values.reshape((-1)) ),3 )
acc = np.round( accuracy_score(train2[['d1','d2','d3','d4']].values.reshape((-1)),(train2[['o1','o2','o3','o4']].values>0.5).astype(int).reshape((-1)) ),3 )
print('AUC =',auc, end='')
print(', ACC =',acc) 
