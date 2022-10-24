# Scores of top teams over time
plt.rcParams["font.size"] = "12"
ALL_TEAMS = df.columns.values
df_ffill = df[ALL_TEAMS].ffill()

# This is broken
df_ffill.T.sample(1000).T.plot(figsize=(20, 10),
                           color=color_pal[0],
                           legend=False,
                           alpha=0.05,
                           ylim=(0.925, TOP_SCORE+0.001),
                           title='All Teams Public LB Scores over Time')

df.ffill().max(axis=1).plot(color=color_pal[1], label='1st Place Public LB', legend=True)
plt.show()
