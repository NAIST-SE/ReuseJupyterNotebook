from catboost import CatBoostRegressor, Pool

ITERATIONS = 200000

FEATURES = [#'atom_index_0',
            'atom_index_1',
            'atom_0',
            'x_0', 'y_0', 'z_0',
            'atom_1', 
            'x_1', 'y_1', 'z_1',
            'dist', 'dist_to_type_mean',
            'atom_count',
            'type']
TARGET = 'scalar_coupling_constant'
CAT_FEATS = ['atom_0','atom_1','type']

train_dataset = Pool(data=train_df[FEATURES],
                  label=train_df['scalar_coupling_constant'].values,
                  cat_features=CAT_FEATS)

cb_model = CatBoostRegressor(iterations=ITERATIONS,
                             learning_rate=0.2,
                             depth=7,
                             eval_metric='MAE',
                             random_seed = 529,
                             task_type="GPU")

# Fit the model
cb_model.fit(train_dataset, verbose=1000)

# Predict
test_data = test_df[FEATURES]

test_dataset = Pool(data=test_data,
                    cat_features=CAT_FEATS)

ss = pd.read_csv('../input/sample_submission.csv')
ss['scalar_coupling_constant'] = cb_model.predict(test_dataset)
ss.to_csv('basline_catboost_submission.csv', index=False)
