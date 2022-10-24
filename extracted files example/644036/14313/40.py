from catboost import Pool, cv

RUN_CATBOOST_CV = False

if RUN_CATBOOST_CV:
    labels = train_df['scalar_coupling_constant'].values
    cat_features = ['type','atom_count','atom_0','atom_1']
    cv_data = train_df[['type','atom_count','atom_0','atom_1',
                        'x_0','y_0','z_0','x_1','y_1','z_1','dist']]
    cv_dataset = Pool(data=cv_data,
                      label=labels,
                      cat_features=cat_features)

    ITERATIONS = 100000
    params = {"iterations": ITERATIONS,
              "learning_rate" : 0.02,
              "depth": 7,
              "loss_function": "MAE",
              "verbose": False,
              "task_type" : "GPU"}

    scores = cv(cv_dataset,
                params,
                fold_count=5, 
                plot="True")
    
    scores['iterations'] = scores['iterations'].astype('int')
    scores.set_index('iterations')[['test-MAE-mean','train-MAE-mean']].plot(figsize=(15, 5), title='CV (MAE) Score by iteration (5 Folds)')
