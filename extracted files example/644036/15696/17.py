fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(16, 4))
train['S'].plot(kind='hist', ax=ax1,
                title='Distribution of Speed',
                bins=20,
                color=color_pal[0])
train['A'].plot(kind='hist',
                ax=ax2,
                title='Distribution of Acceleration',
                bins=20,
                color=color_pal[1])
train['Dis'].plot(kind='hist',
                  ax=ax3,
                  title='Distribution of Distance',
                  bins=20,
                  color=color_pal[2])
plt.show()
