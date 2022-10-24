# Expand Sequence Features
for n in range(107):
    train[f'sequence_{n}'] = train['sequence'].apply(lambda x: x[n]).astype('category')
    test[f'sequence_{n}'] = test['sequence'].apply(lambda x: x[n]).astype('category')

SEQUENCE_COLS = [c for c in train.columns if 'sequence_' in c]

for target in ['reactivity','deg_Mg_pH10','deg_Mg_50C']:

    X = train[SEQUENCE_COLS]
    y = train[f'mean_{target}']
    X_test = test[SEQUENCE_COLS]

    X_train, X_val, y_train, y_val = train_test_split(X, y)

    reg = lgb.LGBMRegressor(n_estimators=1000)
    reg.fit(X_train, y_train,
            eval_set=(X_val, y_val),
           early_stopping_rounds=100,
           verbose=100)

    test[f'mean_{target}_pred'] = reg.predict(X_test)
