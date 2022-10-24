# Pairplot of Regular Season Games
# Only include teams who are both seeded in the tournament
regseason_in_tourney = regseasoncompactresults.dropna(subset=['WSeed','LSeed'])
sns.pairplot(data = regseason_in_tourney,
             vars=['WScore','LScore','WSeed','LSeed'],
             hue='WSeed')
