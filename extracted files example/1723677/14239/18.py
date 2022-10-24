sub = pd.read_csv('../input/sample_submission.csv')

if np.allclose(useful_train,useful_public) & np.allclose(useful_train,useful_private):
    print('We are submitting TRUE predictions for LB 0.950')
    sub['target'] = (test_preds_NN + test_preds_SVM) / 2.0
else:
    print('We are submitting ALL ZERO predictions for LB 0.500')
    sub['target'] = np.zeros( len(sub) )
    
sub.to_csv('submission.csv',index=False)
