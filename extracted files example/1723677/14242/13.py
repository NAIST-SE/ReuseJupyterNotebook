if LOCAL_VALIDATION:
    import xgboost as xgb
    print("XGBoost version:", xgb.__version__)

    xgb_parms = { 
        'n_estimators':2000,
        'max_depth':12, 
        'learning_rate':0.02, 
        'subsample':0.8,
        'colsample_bytree':0.4, 
        'missing':-1, 
        'eval_metric':'auc',
        'objective':'binary:logistic',
        'tree_method':'gpu_hist' 
    }
    train = xgb.DMatrix(data=X_train.iloc[:split][cols],label=X_train.iloc[:split]['isFraud'])
    valid = xgb.DMatrix(data=X_train.iloc[split:][cols],label=X_train.iloc[split:]['isFraud'])
    clf = xgb.train(xgb_parms, dtrain=train,
        num_boost_round=2000,evals=[(train,'train'),(valid,'valid')],
        early_stopping_rounds=100,maximize=True,
        verbose_eval=50)
