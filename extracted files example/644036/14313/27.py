train_df.sample(1000).plot(x='atom_count',
                           y='scalar_coupling_constant',
                           kind='scatter',
                           color=color_pal[0],
                           figsize=(20, 5),
                           alpha=0.5)
plt.show()
