train.query("NflIdRusher == NflId") \
    .groupby('DisplayName')['Yards'] \
    .agg(['count','mean']) \
    .query('count > 100') \
    .sort_values('mean', ascending=True) \
    .tail(10)['mean'] \
    .plot(kind='barh',
          figsize=(15, 5),
          color=color_pal[5],
          xlim=(0,6),
          title='Top 10 Players by Average Yards')
plt.show()
train.query("NflIdRusher == NflId") \
    .groupby('DisplayName')['Yards'] \
    .agg(['count','mean']) \
    .query('count > 100') \
    .sort_values('mean', ascending=True) \
    .head(10)['mean'] \
    .plot(kind='barh',
          figsize=(15, 5),
          color=color_pal[0],
          xlim=(0,6),
          title='Bottom 10 Players by Average Yards')
plt.show()
