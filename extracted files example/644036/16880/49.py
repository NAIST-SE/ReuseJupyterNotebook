fig, ax = plt.subplots(1,1, figsize=(10, 10))
sns.scatterplot(x='avg_pred_raw', y='max_pred_raw', data=metadata.dropna(subset=['avg_pred_raw']), hue='label')
plt.show()
