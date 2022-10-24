train_expanded['1_roll'] = pd.to_numeric(train_expanded['1_roll'])
train_expanded['1_roll'] \
    .dropna() \
    .plot(kind='hist',
          figsize=(15, 3),
          bins=100,
          title='Distribution of First car roll',
          color=my_pal[3])
plt.show()
