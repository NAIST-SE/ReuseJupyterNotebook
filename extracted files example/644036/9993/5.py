train_expanded.groupby('1_model_type')['ImageId'] \
    .count() \
    .sort_values() \
    .plot(kind='barh',
          figsize=(15, 8),
          title='First Car, Count by Model Type',
          color=my_pal[0])
plt.show()
