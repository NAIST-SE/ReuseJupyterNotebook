from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.metrics import roc_auc_score
import matplotlib.pyplot as plt

oof = np.zeros(len(train))
rskf = RepeatedStratifiedKFold(n_splits=25, n_repeats=5)
for train_index, test_index in rskf.split(train.iloc[:,:-1], train['target']):
    clf = LogisticRegression(solver='liblinear',penalty='l1',C=0.1,class_weight='balanced')
    clf.fit(train.loc[train_index].iloc[:,:-1],train.loc[train_index]['target'])
    oof[test_index] += clf.predict_proba(train.loc[test_index].iloc[:,:-1])[:,1]
aucTR = round(roc_auc_score(train['target'],oof),5)
print('CV =',aucTR)
