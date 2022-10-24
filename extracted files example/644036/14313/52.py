plt.rcParams["font.size"] = "12"
# Create Top Teams List
TOP_TEAMS = df.min().loc[df.min() < FIFTYTH_SCORE].index.values
df[TOP_TEAMS].min().sort_values(ascending=False).plot(kind='barh',
                                       xlim=(FIFTYTH_SCORE+0.1,TOP_SCORE-0.1),
                                       title='Top 50 Public LB Teams',
                                       figsize=(12, 15),
                                       color=color_pal[3])
plt.show()
