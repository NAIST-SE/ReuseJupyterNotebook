MEvents.loc[MEvents['PlayerID'] == 2825].groupby('EventType')['EventID'].count() \
    .sort_values() \
    .plot(kind='barh',
          figsize=(15, 5),
          title='Zion Williamson event type count',
          color=mypal[1])
plt.show()
