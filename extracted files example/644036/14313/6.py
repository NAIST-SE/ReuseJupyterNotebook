# Number of of atoms in molecule
fig, ax = plt.subplots(1, 2)
train_df.groupby('molecule_name').count().sort_values('id')['id'].plot(kind='hist',
                                                                       bins=25,
                                                                       color=color_pal[6],
                                                                      figsize=(20, 5),
                                                                      title='# of Atoms in Molecule (Train Set)',
                                                                      ax=ax[0])
test_df.groupby('molecule_name').count().sort_values('id')['id'].plot(kind='hist',
                                                                       bins=25,
                                                                       color=color_pal[2],
                                                                      figsize=(20, 5),
                                                                      title='# of Atoms in Molecule (Test Set)',
                                                                     ax=ax[1])
plt.show()
