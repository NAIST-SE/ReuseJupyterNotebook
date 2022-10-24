train.groupby('GameId')['PlayId'] \
    .nunique() \
    .plot(kind='hist', figsize=(15, 5),
         title='Distribution of Plays per GameId',
         bins=50)
plt.show()
