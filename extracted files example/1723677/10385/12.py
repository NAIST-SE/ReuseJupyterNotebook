# SAVE PREDICTIONS TO CSV    
print('Test predictions saved as submission.csv')
print('OOF predictions saved as oof_submission.csv')
print('Histogram of test predictions displayed below:')

sub = train2[['ID_code','target']].copy()
sub['predict'] = ensemble_preds
sub.reset_index(inplace=True)
sub.sort_values('index',inplace=True)
sub.to_csv('oof_submission.csv',index=False)

test_preds = logr.predict(all_preds[:,:num_vars+1])
sub = pd.read_csv('../input/sample_submission.csv')
sub['target'] = test_preds
sub.to_csv('submission.csv',index=False)

# DISPLAY HISTOGRAM OF PREDICTIONS
b = plt.hist(sub['target'], bins=200)
