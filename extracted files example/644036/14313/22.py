fig, ax = plt.subplots(2, 2, figsize=(20, 10))
scc['fc'].plot(kind='hist', ax=ax.flat[0], bins=500, title='Fermi Contact contribution', color=color_pal[0])
scc['sd'].plot(kind='hist', ax=ax.flat[1], bins=500, title='Spin-dipolar contribution', color=color_pal[1])
scc['pso'].plot(kind='hist', ax=ax.flat[2], bins=500, title='Paramagnetic spin-orbit contribution', color=color_pal[2])
scc['dso'].plot(kind='hist', ax=ax.flat[3], bins=500, title='Diamagnetic spin-orbit contribution', color=color_pal[3])
plt.show()