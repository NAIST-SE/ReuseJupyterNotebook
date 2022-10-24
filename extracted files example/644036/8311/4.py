# Pairplot of the Tourney Seed and Scores
sns.pairplot(tourneycompactresults[['WScore',
                                    'LScore',
                                    'ScoreDiff',
                                    'WSeed',
                                    'LSeed',
                                    'Season']], hue='Season')
