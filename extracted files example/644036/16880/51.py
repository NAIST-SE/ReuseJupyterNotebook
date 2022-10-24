for i, d in metadata.groupby('label'):
    d['avg_pred_raw'].plot(kind='hist',
                           figsize=(15, 5),
                           bins=20,
                           alpha=0.8,
                           title='Average Prediction distribution raw')
    plt.legend(['FAKE','REAL'])
plt.show()
for i, d in metadata.groupby('label'):
    d['max_pred_raw'].plot(kind='hist',
                           figsize=(15, 5),
                           bins=20,
                           title='Max Prediction distribution raw',
                           alpha=0.8)
    plt.legend(['FAKE','REAL'])
plt.show()
