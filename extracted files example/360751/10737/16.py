# submit
sub = pd.read_csv('../input/sample_submission.csv', index_col=['qid'], nrows=numrows)
sub['prediction'] = test_pred > thresh
sub.to_csv("submission.csv")
