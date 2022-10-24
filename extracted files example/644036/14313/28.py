train_df.groupby('type')['scalar_coupling_constant'].mean().plot(kind='barh',
                                                                 figsize=(15, 5),
                                                                title='Average Scalar Coupling Constant by Type')
plt.show()
# THIS IS A MODEL!!! This is a model??
type_mean_dict = train_df.groupby('type')['scalar_coupling_constant'].mean().to_dict()
test_df['scalar_coupling_constant'] = test_df['type'].map(type_mean_dict)
test_df[['id','scalar_coupling_constant']].to_csv('super_simple_submission.csv', index=False)
