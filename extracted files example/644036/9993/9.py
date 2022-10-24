train_expanded['1_x'] = pd.to_numeric(train_expanded['1_x'])
train_expanded['1_y'] = pd.to_numeric(train_expanded['1_y'])
train_expanded['1_z'] = pd.to_numeric(train_expanded['1_z'])
train_expanded['1_x'] \
    .dropna() \
    .plot(kind='hist',
          figsize=(15, 3),
          bins=100,
          title='Distribution of x',
          color=my_pal[0])
plt.show()
train_expanded['1_y'] \
    .dropna() \
    .plot(kind='hist',
          figsize=(15, 3),
          bins=100,
          title='Distribution of y',
          color=my_pal[1])
plt.show()
train_expanded['1_z'] \
    .dropna() \
    .plot(kind='hist',
          figsize=(15, 3),
          bins=100,
          title='Distribution of z',
          color=my_pal[2])
plt.show()
