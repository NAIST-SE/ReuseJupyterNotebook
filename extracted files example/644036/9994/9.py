bmd.groupby('year_built')['site_id'] \
    .count() \
    .plot(figsize=(15, 5),
          style='.-',
          title='Building Meta Data - Count by Year Built')
plt.show()
print('{} Buildings have no year data.'.format(np.sum(bmd['year_built'].isna())))
