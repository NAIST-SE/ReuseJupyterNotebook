fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(16, 4))
train.query("NflIdRusher == NflId")['S'] \
    .plot(kind='hist',
          ax=ax1,
          title='Distribution of Speed (Ball Carrier Only)',
          bins=20,
          color=color_pal[0])
train.query("NflIdRusher == NflId")['A'] \
    .plot(kind='hist',
          ax=ax2,
          title='Distribution of Acceleration (Ball Carrier Only)',
          bins=20,
          color=color_pal[1])
train.query("NflIdRusher == NflId")['Dis'] \
    .plot(kind='hist',
          ax=ax3,
          title='Distribution of Distance (Ball Carrier Only)',
          bins=20,
          color=color_pal[2])
plt.show()
