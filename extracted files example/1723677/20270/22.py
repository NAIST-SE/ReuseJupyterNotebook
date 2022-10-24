all = []
for k in range(x.shape[1]):
    auc = roc_auc_score(OOF_CSV[0].target,x[:,k])
    all.append(auc)
    print('Model %i has OOF AUC = %.4f'%(k,auc))
    
m = [np.argmax(all)]; w = []
