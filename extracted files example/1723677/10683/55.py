print('Converting data to Model Two...')
df_trainC = df_trainC.copy()
df_trainD = df_trainD.copy()
for col in cols: relax_data(df_trainC, df_trainD, col)
categorize(df_trainC, df_trainD, cols)
model = lgb.LGBMClassifier(n_estimators=3000, colsample_bytree=0.2, objective='binary', num_leaves=16,
          max_depth=-1, learning_rate=0.1)
h=model.fit(df_trainC[cols], df_trainC['HasDetections'], eval_metric='auc',
          eval_set=[(df_trainD[cols], df_trainD['HasDetections'])], verbose=250,
          early_stopping_rounds=100)
