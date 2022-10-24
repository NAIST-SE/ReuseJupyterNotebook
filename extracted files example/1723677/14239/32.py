sub = pd.read_csv('../input/sample_submission.csv')
sub['target'] = all_preds
sub.to_csv('submission.csv',index=False)

plt.hist( test_pred ,bins=100)
plt.title('Model 512 test predictions')
plt.show()
