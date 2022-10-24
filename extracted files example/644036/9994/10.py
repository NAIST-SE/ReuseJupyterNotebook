bmd.groupby('primary_use') \
    .count()['site_id'] \
    .sort_values() \
    .plot(kind='barh',
          figsize=(15, 5),
          title='Count of Buildings by Primary Use')
plt.show()
