import xgboost as xgb
print("XGBoost version:", xgb.__version__)
from sklearn.model_selection import GroupKFold
from sklearn.metrics import roc_auc_score

X_test = X_test.sort_index()
oof = np.zeros(len(X_train))
preds = np.zeros(len(X_test))

skf = GroupKFold(n_splits=6)
for i, (idxT, idxV) in enumerate( skf.split(X_train, X_train.isFraud, groups=X_train['DT_M'].to_pandas()) ):
    month = X_train.iloc[idxV]['DT_M'].iloc[0]
    print('Fold',i,'withholding month',month)
    print(' rows of train =',len(idxT),'rows of holdout =',len(idxV))
        
    xgb_parms = { 
        'max_depth':12, 
        'learning_rate':0.02, 
        'subsample':0.8,
        'colsample_bytree':0.4, 
        'missing':-1, 
        'eval_metric':'auc',
        'objective':'binary:logistic',
        'tree_method':'gpu_hist' 
    }
    train = xgb.DMatrix(data=X_train.iloc[idxT][cols],label=X_train.iloc[idxT]['isFraud'])
    valid = xgb.DMatrix(data=X_train.iloc[idxV][cols],label=X_train.iloc[idxV]['isFraud'])
    clf = xgb.train(xgb_parms, dtrain=train,
        num_boost_round=2000,evals=[(train,'train'),(valid,'valid')],
        early_stopping_rounds=200,maximize=True,
        verbose_eval=100)   
    
    oof[idxV] += clf.predict(valid)
    test = xgb.DMatrix(data=X_test[cols])
    preds += clf.predict(test)/skf.n_splits
    del clf; x=gc.collect()
print('#'*20)
print ('XGB96 OOF CV=',roc_auc_score(X_train.isFraud.to_array(),oof))
