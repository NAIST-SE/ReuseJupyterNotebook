# Make Submission
ss = pd.read_csv('../input/stanford-covid-vaccine/sample_submission.csv')
ss_new[ss.columns].to_csv('submission_lgbm_v1.csv', index=False)
