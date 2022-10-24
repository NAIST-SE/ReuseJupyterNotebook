TARGETS = ['reactivity','deg_Mg_pH10','deg_Mg_50C']
for i, t in enumerate(TARGETS):
    ss_new[t].plot(kind='hist',
                              figsize=(10, 3),
                              bins=100,
                              color=color_pal[i*3],
                              title=f'Submission {t}')
    plt.show()
