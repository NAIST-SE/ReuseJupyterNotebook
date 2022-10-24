test['vlads_rank'] = test['vlads_preds'].rank(method='first')
test['qda_rank'] = test['qda_preds_target'].rank(method='first')
test.plot(x='vlads_rank', y='qda_rank', kind='scatter', figsize=(15, 15), alpha=0.2, title='Vlads public test preds vs QDA by Rank')
plt.show()
