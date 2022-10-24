# Scores of top teams over time
ALL_TEAMS = [x for x in df.columns.values if x != 'nan']
df[ALL_TEAMS].ffill().plot(figsize=(20, 10),
                           color=color_pal[0],
                           legend=False,
                           alpha=0.05,
                           ylim=(0.94,TOP_SCORE+0.001),
                           title='All Teams Public LB Scores over Time')
df.ffill().max(axis=1).plot(color=color_pal[1], label='1st Place Public LB', legend=True)
plt.show()
