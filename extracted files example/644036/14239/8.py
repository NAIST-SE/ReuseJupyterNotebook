fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(15, 10))
test['qda_preds_target'] = preds
test['vlads_preds'] = vlad_preds[0:131073]
test[['qda_preds_target','vlads_preds']].sort_values('qda_preds_target').reset_index(drop=True) \
    .plot(style='.', alpha=0.1,
          title='Vlad 0.973 Public Test predictions vs. QDA - Ordered by QDA',
          ax=ax1)
test[['qda_preds_target','vlads_preds']].sort_values('vlads_preds').reset_index(drop=True) \
    .plot(style='.', alpha=0.1,
          title='Vlad 0.973 Public Test predictions vs. QDA - Ordered by Vlads',
          ax=ax2)
plt.show()
