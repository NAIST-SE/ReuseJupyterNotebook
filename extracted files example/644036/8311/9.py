# Teams with the Most Losses
count_of_losses = regseasoncompactresults.groupby('LTeamID')['LTeamID'].agg('count')
count_of_losses = count_of_losses.sort_values(ascending=False)
team_loss_count = pd.DataFrame(count_of_losses).merge(teams, left_index=True, right_on='TeamID')[['TeamName','LTeamID']]
team_loss_count.rename(columns={'LTeamID':'Loss Count'}).head(10)

# These teams aren't super great at basketball
