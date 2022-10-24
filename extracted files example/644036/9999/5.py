# Data prep
train['store_item'] = train['store_name'] + '-' + train['item_name']
train['store_item_mean'] = train.groupby('store_item')['sales'].transform('mean')
train['deviation_from_storeitem_mean'] = train['sales'] - train['store_item_mean']
train['dev_rolling'] = train.groupby('store_item')['deviation_from_storeitem_mean'].rolling(30).mean().reset_index()['deviation_from_storeitem_mean']
train_pivoted = train.pivot(index='store_item', columns='date', values='sales')
train_pivoted.head()
