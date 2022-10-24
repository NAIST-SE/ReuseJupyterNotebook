train['revenue'].plot(kind='hist',
                      figsize=(15, 5),
                      bins=50,
                      title='Distribution of Revenue (Train Set)')
plt.show()
print('Revenue has mean {:1.0f} and standard deviation {:1.0f}'.format(train['revenue'].mean(), train['revenue'].std())) 
