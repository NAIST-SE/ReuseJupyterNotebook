fig, axes = plt.subplots(4, 1, figsize=(15, 8), sharex=True)
n = 0
for i, d in train.groupby('Down'):
    d['Yards'].plot(kind='hist',
                    bins=30,
                   color=color_pal[n],
                   ax=axes[n],
                   title=f'Yards Gained on down {i}')
    n+=1
