# Expand Sequence Features
for n in range(107):
    train[f'structure_{n}'] = train['structure'].apply(lambda x: x[n]).astype('category')
    test[f'structure_{n}'] = test['structure'].apply(lambda x: x[n]).astype('category')
    train[f'predicted_loop_type_{n}'] = train['predicted_loop_type'].apply(lambda x: x[n]).astype('category')
    test[f'predicted_loop_type_{n}'] = test['predicted_loop_type'].apply(lambda x: x[n]).astype('category')
    train[f'sequence_{n}'] = train['sequence'].apply(lambda x: x[n]).astype('category')
    test[f'sequence_{n}'] = test['sequence'].apply(lambda x: x[n]).astype('category')

SEQUENCE_COLS = [c for c in train.columns if 'sequence_' in c]
STRUCTURE_COLS = [c for c in train.columns if 'structure_' in c]
PLT_COLS = [c for c in train.columns if 'predicted_loop_type_' in c]

for target in ['reactivity','deg_Mg_pH10','deg_Mg_50C']:

    X = train[SEQUENCE_COLS + STRUCTURE_COLS + PLT_COLS]
    y = train[f'mean_{target}']
    X_test = test[SEQUENCE_COLS + STRUCTURE_COLS + PLT_COLS]

    X_train, X_val, y_train, y_val = train_test_split(X, y)

    reg = lgb.LGBMRegressor(n_estimators=10000,
                            learning_rate=0.001,
                            feature_fraction=0.8)
    reg.fit(X_train, y_train,
            eval_set=(X_val, y_val),
           early_stopping_rounds=100,
           verbose=1000)

    test[f'mean_{target}_pred'] = reg.predict(X_test)
    
ss['id'] = 'id_' + ss['id_seqpos'].str.split('_', expand=True)[1]

# Merge my predicted average values
ss_new = ss. \
    drop(['reactivity','deg_Mg_pH10','deg_Mg_50C'], axis=1) \
    .merge(test[['id',
               'mean_reactivity_pred',
               'mean_deg_Mg_pH10_pred',
               'mean_deg_Mg_50C_pred']] \
               .rename(columns={'mean_reactivity_pred' : 'reactivity',
                                'mean_deg_Mg_pH10_pred': 'deg_Mg_pH10',
                                'mean_deg_Mg_50C_pred' : 'deg_Mg_50C'}
                      ),
         on='id',
        validate='m:1')

ss = pd.read_csv('../input/stanford-covid-vaccine/sample_submission.csv')
ss_new[ss.columns].to_csv('submission.csv', index=False)

TARGETS = ['reactivity','deg_Mg_pH10','deg_Mg_50C']
for i, t in enumerate(TARGETS):
    ss_new[t].plot(kind='hist',
                              figsize=(10, 3),
                              bins=100,
                              color=color_pal[i*3],
                              title=f'Submission {t}')
    plt.show()
