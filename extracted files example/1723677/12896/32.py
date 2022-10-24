train = pd.read_csv('../input/train.csv')
ct = 0
for i in range(300):
    auc = roc_auc_score(train['target'],train[str(i)])
    if (auc<low)|(auc>high): ct += 1   
print('There are',ct,'real variables with AUC less than',low,'or greater than',high)
a = round(ct-hg,1); b = round(ct-lw,1)
print('Therefore we are 80% confident that between',a,'and',b,
      'real variables are useful with AUC less than',low,'or greater than',high)
print('Additionally there are possible useful real variables with weak AUC between',low,'and',high)
