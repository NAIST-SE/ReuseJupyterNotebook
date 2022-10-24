# Teams with the Most Wins
count_of_wins = regseasoncompactresults.groupby('WTeamID')['WTeamID'].agg('count')
count_of_wins = count_of_wins.sort_values(ascending=False)
team_wins_count = pd.DataFrame(count_of_wins).merge(teams, left_index=True, right_on='TeamID')[['TeamName','WTeamID']]
team_wins_count.rename(columns={'WTeamID':'Win Count'}).head(10)
# These teams are super good at basketball
