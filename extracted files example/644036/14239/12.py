test[['vlads_preds','qda_preds_target','diff']] \
    .sort_values('diff') \
    .reset_index(drop=True) \
    .plot(style='.', figsize=(15, 5), title='Plot Predictions sorted by difference')
plt.show()
