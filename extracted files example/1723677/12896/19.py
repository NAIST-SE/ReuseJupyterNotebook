test = pd.read_csv('../input/test.csv')
pred = test.iloc[:,1:].values.dot(df['A'].values)
sub = pd.read_csv('../input/sample_submission.csv')
sub['target'] = pred
sub.to_csv('submission.csv',index=False)
