# Lets just try the first 10 features
for feature in features[:10]:
    train.plot(x='target', y=feature, figsize=(10,1), kind='scatter', title=feature)
    plt.axis('off')
