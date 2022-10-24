plt.rcParams["font.size"] = "12"
ax =df.ffill() \
    .count(axis=1) \
    .plot(figsize=(20, 8),
          title='Number of Teams in the Competition by Date',
         color=color_pal[5], lw=5)
ax.set_ylabel('Number of Teams')
plt.axvline('09-23-2019', color='orange', linestyle='-.')
plt.text('09-23-2019', 4000,'Merger Deadline',rotation=-90)
plt.axvline('10-1-2019', color='orange', linestyle='-.')
plt.text('10-1-2019', 4000,'Original Deadline',rotation=-90)
plt.axvline('10-3-2019', color='orange', linestyle='-.')
plt.text('10-3-2019', 4000,'Extended Deadline',rotation=-90)
plt.show()
