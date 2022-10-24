fig, ax = plt.subplots(1,1, figsize=(10, 10))
sns.scatterplot(x='avg_pred_c23', y='max_pred_c23', data=metadata.dropna(subset=['avg_pred_c23']), hue='label')
plt.show()
