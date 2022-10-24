plt.rcParams["font.size"] = "13"
ax = df.ffill() \
    .count(axis=1) \
    .plot(figsize=(20, 8),
          title='Number of Teams in the Competition by Date',
          color=color_pal[5], lw=5)
ax.set_ylabel('Number of Teams')
#ax.set_ylim('2019-10-01','2019-11-30')
plt.axvline('11-20-2019', color='orange', linestyle='-.')
#plt.text('11-20-2019', 0.1,'Merger Deadline',rotation=-90)
plt.axvline('11-27-2019', color='orange', linestyle='-.')
#plt.text('11-27-2019', 40,'Deadline',rotation=-90)
plt.show()
