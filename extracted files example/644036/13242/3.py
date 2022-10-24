y_train['count'] = 1
y_train.groupby('surface').sum()['count'] \
    .sort_values(ascending=True) \
    .plot(kind='barh', color='grey', figsize=(15, 5), title='Count of Surface Type')
plt.show()
