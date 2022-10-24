# Teams with the Most Wins
count_of_wins2017 = regseason2017.groupby('WTeamID')['WTeamID'].agg('count')
count_of_wins2017 = count_of_wins2017.sort_values(ascending=False)
team_wins_count2017 = pd.DataFrame(count_of_wins2017).merge(teams, left_index=True, right_on='TeamID')[['TeamName','WTeamID']]
team_wins_count2017 = team_wins_count2017.rename(columns={'WTeamID':'Win Count'})

count_of_losses2017 = regseason2017.groupby('LTeamID')['LTeamID'].agg('count')
count_of_losses2017 = count_of_losses2017.sort_values(ascending=False)
team_losses_count2017 = pd.DataFrame(count_of_losses2017).merge(teams, left_index=True, right_on='TeamID')[['TeamName','LTeamID']]
team_losses_count2017 = team_losses_count2017.rename(columns={'LTeamID':'Loss Count'})

winloss2017 = pd.merge(team_wins_count2017, team_losses_count2017, how='outer')
winloss2017.sort_values('Win Count', ascending=False).head(26)
winloss2017 = winloss2017.fillna(0)
winloss2017.head(15)
