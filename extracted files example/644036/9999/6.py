deviation_pivot = train.pivot(index='store_item', columns='date', values='dev_rolling')
deviation_pivot = deviation_pivot.dropna(axis=1)
deviation_pivot.head()
