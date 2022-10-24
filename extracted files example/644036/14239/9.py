test['diff'] = test['vlads_preds'] - test['qda_preds_target']
test['diff'].plot(kind='hist', figsize=(15, 5), bins=200, title='Distribution of difference between Vlad and Simple QDA preds')
plt.show()
