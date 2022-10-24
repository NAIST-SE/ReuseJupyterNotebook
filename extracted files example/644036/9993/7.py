train_expanded['1_pitch'] = pd.to_numeric(train_expanded['1_pitch'])
train_expanded['1_pitch'] \
    .dropna() \
    .plot(kind='hist',
          figsize=(15, 3),
          bins=100,
          title='Distribution of First car pitch',
          color=my_pal[2])
plt.show()
