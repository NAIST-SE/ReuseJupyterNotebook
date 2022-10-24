color_index = 0
axes_index = 0
fig, axes = plt.subplots(8, 1, figsize=(20, 20), sharex=True)
for mtype, d in train_df.groupby('type'):
    d['dist'].plot(kind='hist',
                  bins=1000,
                  title='Distribution of Distance Feature for {}'.format(mtype),
                  color=color_pal[color_index],
                  ax=axes[axes_index])
    if color_index == 6:
        color_index = 0
    else:
        color_index += 1
    axes_index += 1
plt.show()
