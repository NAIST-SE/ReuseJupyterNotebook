scc.groupby('type').count()['molecule_name'].sort_values().plot(kind='barh',
                                                                color='grey',
                                                               figsize=(15, 5),
                                                               title='Count of Coupling Type in Train Set')
plt.show()
