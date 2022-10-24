train['budget'].plot(kind='hist',
                      figsize=(15, 5),
                      bins=50,
                      title='Distribution of Budget (Train Set)',
                      color='blue')
plt.show()

# Use the log1p transform since some values are zero
train['budget_log'] = train['budget'].apply(np.log)
train['budget_log'] = train['budget_log'].replace(-np.inf, 0)
train['budget_log'].plot(kind='hist',
                      figsize=(15, 5),
                      bins=50,
                      title='Distribution of Log+1 Budget (Train Set)',
                      color='blue')
plt.show()
