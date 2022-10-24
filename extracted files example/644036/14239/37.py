ax =df.ffill() \
    .count(axis=1) \
    .plot(figsize=(20, 8),
          title='Number of Teams in the Competition by Date',
         color=color_pal[5], lw=5)
ax.set_ylabel('Number of Teams')
plt.show()
