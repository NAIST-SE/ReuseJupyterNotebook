genre_list = genres.columns.values
for genre in genre_list:
    if len(train.loc[train[genre] == 1]) > 500:
        fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))
        train.loc[train[genre] == 1]['budget_log'].plot(kind='hist', figsize=(15, 2), bins=50, title='{} Log Budget'.format(genre), ax=ax1, xlim=(0, 25))
        train.loc[train[genre] == 1]['revenue_log'].plot(kind='hist', figsize=(15, 2), bins=50, title='{} Log Revenue'.format(genre), ax=ax2, xlim=(0, 25))
        train.loc[train[genre] == 1].plot(x='budget_log', y='revenue_log', kind='scatter', ax=ax3)
        plt.show()
