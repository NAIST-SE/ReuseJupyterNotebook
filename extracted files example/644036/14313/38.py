if RUN_LGB:
    # Save Prediction and name appropriately
    submission_csv_name = 'submission_lgb_{}folds_{}CV.csv'.format(n_fold, np.mean(scores))
    oof_csv_name = 'oof_lgb_{}folds_{}CV.csv'.format(n_fold, np.mean(scores))
    fi_csv_name = 'fi_lgb_{}folds_{}CV.csv'.format(n_fold, np.mean(scores))

    print('Saving LGB Submission as:')
    print(submission_csv_name)
    ss = pd.read_csv('../input/sample_submission.csv')
    ss['scalar_coupling_constant'] = prediction
    ss.to_csv(submission_csv_name, index=False)
    ss.head()
    # OOF
    oof_df = train_df[['id','molecule_name','scalar_coupling_constant']].copy()
    oof_df['oof_pred'] = oof
    oof_df.to_csv(oof_csv_name, index=False)
    # Feature Importance
    feature_importance.to_csv(fi_csv_name, index=False)
