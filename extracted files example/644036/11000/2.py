# Scores of top teams over time
ALL_TEAMS = df.columns.values
df[ALL_TEAMS].ffill().plot(figsize=(20, 10),
                           ylim=(1.0, 1.8),
                           color=color_pal[0],
                           legend=False,
                           alpha=0.01,
                           title='All LANL Teams Scores over Time')
plt.show()
