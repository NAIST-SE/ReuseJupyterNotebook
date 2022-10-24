fig, axes = plt.subplots(3, 2, constrained_layout=True, figsize=(15 , 10))
#fig.tight_layout()
ax_idx = 0
ax_idx2 = 0
for i in range(4, 10):
    this_ax = axes[ax_idx2][ax_idx]
    #print(ax_idx, ax_idx2)
    sns.distplot(train.query('DefendersInTheBox == @i')['Yards'],
                ax=this_ax,
                color=color_pal[ax_idx2])
    this_ax.set_title(f'{i} Defenders in the box')
    this_ax.set_xlim(-10, 20)
    ax_idx += 1
    if ax_idx == 2:
        ax_idx = 0
        ax_idx2 += 1
plt.show()
