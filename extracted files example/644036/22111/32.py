train = pd.read_json('../input/stanford-covid-vaccine/train.json', lines=True)
test = pd.read_json('../input/stanford-covid-vaccine/test.json', lines=True)
ss = pd.read_csv('../input/stanford-covid-vaccine/sample_submission.csv')

train_expanded, SEQUENCE_COLS, STRUCTURE_COLS = expand_columns(train)
test_expanded, SEQUENCE_COLS, STRUCTURE_COLS = expand_columns(test)
ss = parse_sample_submission(ss)

train_long = get_train_long(train)
test_long = get_test_long(test)

train_long = add_long_features(train_long)
test_long = add_long_features(test_long)

FEATURES = ['seqpos',
            'sequence',
            'structure',
            'predicted_loop_type',
            'A', 'C', 'G', 'U', '(', ')', '.', 'B', 'E',
            'H', 'I', 'M', 'S', 'X',
            'sequence_shift-5', 'structure_shift-5',
            'predicted_loop_type_shift-5', 'sequence_shift-4', 'structure_shift-4',
            'predicted_loop_type_shift-4', 'sequence_shift-3', 'structure_shift-3',
            'predicted_loop_type_shift-3', 'sequence_shift1', 'structure_shift1',
            'predicted_loop_type_shift1', 'sequence_shift2', 'structure_shift2',
            'predicted_loop_type_shift2', 'sequence_shift3', 'structure_shift3',
            'predicted_loop_type_shift3', 'sequence_shift4', 'structure_shift4',
            'predicted_loop_type_shift4', 'sequence_shift5', 'structure_shift5',
            'predicted_loop_type_shift5']

train_long = make_feature_types(train_long, FEATURES)
test_long = make_feature_types(test_long, FEATURES)

train_ids, val_ids = train_test_split(train['id'].unique())

TARGETS = ['reactivity','deg_Mg_pH10','deg_Mg_50C']
fis = []
for t in TARGETS:
    print(f'==== Running for target {t} ====')
    X_train = train_long.dropna(subset=[t]).loc[train_long['id'].isin(train_ids)][FEATURES].copy()
    y_train = train_long.dropna(subset=[t]).loc[train_long['id'].isin(train_ids)][t].copy()
    X_val = train_long.dropna(subset=[t]).loc[train_long['id'].isin(val_ids)][FEATURES].copy()
    y_val = train_long.dropna(subset=[t]).loc[train_long['id'].isin(val_ids)][t].copy()
    X_test = test_long[FEATURES].copy()
    y_train = pd.to_numeric(y_train)
    y_val = pd.to_numeric(y_val)
    
    reg = lgb.LGBMRegressor(n_estimators=10000,
                            learning_rate=0.01,
                            importance_type='gain')
    reg.fit(X_train, y_train,
            eval_set=(X_val, y_val),
           verbose=1000,
           early_stopping_rounds=500)

    fi_df = pd.DataFrame(index=FEATURES, 
                 data=reg.feature_importances_,
                 columns=[f'importance_{t}'])
    
    fi_df.sort_values(f'importance_{t}') \
        .plot(kind='barh', figsize=(8, 15), title=t)
    plt.show()
    fis.append(fi_df)
    
    test_long[f'{t}_pred'] = reg.predict(X_test)
