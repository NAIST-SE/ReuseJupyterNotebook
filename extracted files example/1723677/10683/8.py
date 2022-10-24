import lightgbm as lgb
from sklearn.model_selection import StratifiedKFold

pred_val = np.zeros(len(df_test))
folds = StratifiedKFold(n_splits=5, shuffle=True)

ct = 0
for idxT, idxV in folds.split(df_train[cols+cols2+cols3+cols6], df_train['HasDetections']):
    # TRAIN LGBM
    ct += 1; print('####### FOLD ',ct,'#########')
    df_trainA = df_train.loc[idxT]
    df_trainB = df_train.loc[idxV]
    model = lgb.LGBMClassifier(n_estimators=10000, colsample_bytree=0.5, objective='binary', num_leaves=2048,
            max_depth=-1, learning_rate=0.04)
    h=model.fit(df_trainA[cols+cols2+cols3+cols6+cols8], df_trainA['HasDetections'], eval_metric='auc',
            eval_set=[(df_trainB[cols+cols2+cols3+cols6+cols8], df_trainB['HasDetections'])], verbose=200,
            early_stopping_rounds=100)
    
    # PREDICT TEST
    del df_trainA, df_trainB; x=gc.collect()
    idx = 0; ct2 = 1; chunk = 1000000
    print('Predicting test...')
    while idx < len(df_test):
        idx2 = min(idx + chunk, len(df_test) )
        idx = range(idx, idx2)
        pred_val[idx] += model.predict_proba(df_test.iloc[idx][cols+cols2+cols3+cols6+cols8])[:,1]
        #print('Finished predicting part',ct2)
        ct2 += 1; idx = idx2
