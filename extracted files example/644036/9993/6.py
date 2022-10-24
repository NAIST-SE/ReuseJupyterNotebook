train_expanded['1_yaw'] = pd.to_numeric(train_expanded['1_yaw'])
train_expanded['1_yaw'] \
    .dropna() \
    .plot(kind='hist',
          figsize=(15, 3),
          bins=100,
          title='Distribution of First car YAW',
          color=my_pal[1])
plt.show()
