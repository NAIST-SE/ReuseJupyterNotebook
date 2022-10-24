# Save Submission
submission_csv = 'submission_{:0.2f}CV_{}Folds_{}.csv'.format(roc_auc_score(y_train, oof), N_FOLDS, run_id)
print('Saving submission as {}'.format(submission_csv))
ss.to_csv(submission_csv, index=False)
ss.to_csv('submission.csv', index=False)
# Save Feature Importance
feature_importance_csv = 'fi_{:0.2f}CV_{}Folds_{}.csv'.format(roc_auc_score(y_train, oof), N_FOLDS, run_id)
print('Saving feature importance as {}'.format(feature_importance_csv))
feature_importance_df.to_csv(feature_importance_csv, index=False)

# Save OOF
oof_df = pd.DataFrame()
oof_df['oof'] = oof
oof_df['id'] = id_train
oof_df['target'] = y_train
oof_csv = 'oof_{:0.2f}CV_{}Folds_{}.csv'.format(roc_auc_score(y_train, oof), N_FOLDS, run_id)
print('Saving out-of-fold predictions as {}'.format(oof_csv))
oof_df.to_csv(oof_csv, index=False)
