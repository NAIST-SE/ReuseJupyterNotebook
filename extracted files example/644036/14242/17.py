plt.rcParams["font.size"] = "12"
# Create Top Teams List
TOP_TEAMS = df.max().loc[df.max() > FIFTYTH_SCORE].index.values
df[TOP_TEAMS].max().sort_values(ascending=True).plot(kind='barh',
                                       xlim=(FIFTYTH_SCORE-0.001,TOP_SCORE+0.001),
                                       title='Top 50 Public LB Teams',
                                       figsize=(12, 15),
                                       color=color_pal[3])
plt.show()
