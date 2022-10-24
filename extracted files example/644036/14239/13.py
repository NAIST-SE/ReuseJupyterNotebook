test.plot(x='vlads_preds',
          y='qda_preds_target',
          kind='scatter',
          figsize=(15, 15),
          alpha=0.2,
          title='Vlad Predictions vs QDA')
plt.show()
