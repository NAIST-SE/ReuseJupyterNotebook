import lightgbm as lgb,gc

# CREATE TRAIN AND VALIDATE
X_train = df_train.sample(frac=0.5)
Y_train = X_train['HasDetections']
X_val = df_train[ ~df_train.index.isin(X_train.index) ]
Y_val = X_val['HasDetections']
del X_train['HasDetections'], X_val['HasDetections'], df_train
x=gc.collect()

# TRAIN LGBM
model = lgb.LGBMClassifier(n_estimators=10000, colsample_bytree=0.7, objective='binary', num_leaves=32,
            max_depth=-1, learning_rate=0.1)
h=model.fit(X_train, Y_train, eval_metric='auc', eval_set=[(X_val, Y_val)], verbose=50,
            early_stopping_rounds=100)

# FEATURE IMPORTANCE
df = pd.DataFrame({"mean" : model.feature_importances_, "feature" : X_train.columns })
df.sort_values("mean", inplace=True)
ax = df.plot(x="feature", y="mean", kind='barh',color='green', figsize=(12, 20)
             , title='External Data LGBM Feature Importance')
