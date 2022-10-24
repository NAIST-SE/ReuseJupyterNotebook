train_df.groupby('type')['scalar_coupling_constant'].plot(kind='hist',
                                                          bins=1000,
                                                          figsize=(20, 5),
                                                          alpha=0.8,
                                                         title='scalar_coupling_constant by coupling type')
plt.legend()
plt.show()
