# Create Top Teams List
TOP_TEAMS = df.min().loc[df.min() < 1.35].index.values
df[TOP_TEAMS].min().sort_values().plot(kind='barh',
                                       xlim=(1.0, 1.36),
                                       title='Teams with Scores less than 1.35',
                                       figsize=(12, 15),
                                       color=color_pal[3])
plt.show()
