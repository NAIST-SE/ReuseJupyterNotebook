train['revenue_log'] = train['revenue'].apply(np.log)
train['revenue_log'].plot(kind='hist',
                      figsize=(15, 5),
                      bins=50,
                      title='Distribution of Log Revenue (Train Set)')
plt.show()
