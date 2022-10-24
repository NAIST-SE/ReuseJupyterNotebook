# LightGBM is no bueno

# import lightgbm as lgb

# SEED = 529
# params = {'num_leaves': 8,
#           'min_data_in_leaf': 5,  # 42,
#           'objective': 'regression',
#           'max_depth': 2,
#           'learning_rate': 0.02,
# #           'boosting': 'gbdt',
#           'bagging_freq': 5,  # 5
#           'bagging_fraction': 0.8,  # 0.5,
#           'feature_fraction': 0.82,
#           'bagging_seed': SEED,
#           'reg_alpha': 1,  # 1.728910519108444,
#           'reg_lambda': 4.98,
#           'random_state': SEED,
#           'metric': 'mse',
#           'verbosity': 100,
#           'min_gain_to_split': 0.02,  # 0.01077313523861969,
#           'min_child_weight': 5,  # 19.428902804238373,
#           'num_threads': 6,
#           }

# model = lgb.LGBMRegressor(**params, n_estimators=5000)
# model.fit(train[FEATURES],
#           train[TARGET])
