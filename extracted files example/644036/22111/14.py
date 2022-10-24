fig, axs = plt.subplots(3, 1,
                        figsize=(10, 6),
                        sharex=True)
axs = axs.flatten()
train['mean_reactivity'] = train['reactivity'].apply(lambda x: np.mean(x))
train['mean_deg_Mg_pH10'] = train['deg_Mg_pH10'].apply(lambda x: np.mean(x))
train['mean_deg_Mg_50C'] = train['deg_Mg_50C'].apply(lambda x: np.mean(x))

train['mean_reactivity'] \
    .plot(kind='hist',
          bins=50,
          color=color_pal[0],
          title='Distribution of Mean Reactivity in training set',
         ax=axs[0])
train['mean_deg_Mg_pH10'] \
    .plot(kind='hist',
          bins=50,
          ax=axs[1],
          color=color_pal[4],
          title='Distribution of Mean deg_Mg_pH10 in training set')
train['mean_deg_Mg_50C'] \
    .plot(kind='hist',
          bins=50,
          ax=axs[2],
          color=color_pal[3],
          title='Distribution of Mean deg_Mg_50C in training set')
plt.tight_layout()
plt.show()
