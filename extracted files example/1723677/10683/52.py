import lightgbm as lgb
df_trainA = df_train.sample(frac=0.5)
df_trainB = df_train[ ~df_train.index.isin(df_trainA.index)]
model = lgb.LGBMClassifier(n_estimators=3000, colsample_bytree=0.2, objective='binary', num_leaves=16,
          max_depth=-1, learning_rate=0.1)
h=model.fit(df_trainA[cols], df_trainA['HasDetections'], eval_metric='auc',
          eval_set=[(df_trainB[cols], df_trainB['HasDetections'])], verbose=250,
          early_stopping_rounds=100)
