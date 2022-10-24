fig, ax = plt.subplots(1, 2, figsize=(20, 8))
train.groupby('PlayId') \
    .first() \
    .groupby('OffensePersonnel') \
    .count()['GameId'] \
    .sort_values(ascending=False) \
    .head(15) \
    .sort_values() \
    .plot(kind='barh',
         title='Offense Personnel # of Plays',
         ax=ax[0])
train.groupby('PlayId') \
    .first() \
    .groupby('DefensePersonnel') \
    .count()['GameId'] \
    .sort_values(ascending=False) \
    .head(15) \
    .sort_values() \
    .plot(kind='barh',
         title='Defense Personnel # of Plays',
         ax=ax[1])
plt.show()
