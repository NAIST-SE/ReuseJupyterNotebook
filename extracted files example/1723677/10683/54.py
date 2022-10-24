df_trainC = df_train[ df_train['AvSigVersion2']<275 ]
df_trainD = df_train[ df_train['AvSigVersion2']>=275 ]
model = lgb.LGBMClassifier(n_estimators=3000, colsample_bytree=0.2, objective='binary', num_leaves=16,
          max_depth=-1, learning_rate=0.1)
h=model.fit(df_trainC[cols], df_trainC['HasDetections'], eval_metric='auc',
          eval_set=[(df_trainD[cols], df_trainD['HasDetections'])], verbose=250,
          early_stopping_rounds=100)
