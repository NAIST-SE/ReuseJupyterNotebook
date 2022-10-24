# Calculate the Average Team Seed
averageseed = tourneyseeds.groupby(['TeamID']).agg(np.mean).sort_values('SeedNumber')
averageseed = averageseed.merge(teams, left_index=True, right_on='TeamID') #Add Teamnname
averageseed.head(20).plot(x='TeamName',
                          y='SeedNumber',
                          kind='bar',
                          figsize=(15,5),
                          title='Top 20 Average Tournament Seed',
                          rot=45)
