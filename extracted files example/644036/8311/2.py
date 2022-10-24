# Convert Tourney Seed to a Number
tourneyseeds['SeedNumber'] = tourneyseeds['Seed'].apply(lambda x: int(x[-2:]))

# Credit much of the merge code to Teza (Thanks!)
# https://www.kaggle.com/tejasrinivas/preprocessing-code-to-join-all-the-tables-eda
tourneycompactresults['WSeed'] = \
    tourneycompactresults[['Season','WTeamID']].merge(tourneyseeds,
                                                      left_on = ['Season','WTeamID'],
                                                      right_on = ['Season','TeamID'],
                                                      how='left')[['SeedNumber']]
tourneycompactresults['LSeed'] = \
    tourneycompactresults[['Season','LTeamID']].merge(tourneyseeds,
                                                      left_on = ['Season','LTeamID'],
                                                      right_on = ['Season','TeamID'],
                                                      how='left')[['SeedNumber']]

tourneycompactresults = \
    tourneycompactresults.merge(gamecities,
                                how='left',
                                on=['Season','DayNum','WTeamID','LTeamID'])

regseasoncompactresults['WSeed'] = \
    regseasoncompactresults[['Season','WTeamID']].merge(tourneyseeds,
                                                        left_on = ['Season','WTeamID'],
                                                        right_on = ['Season','TeamID'],
                                                        how='left')[['SeedNumber']]
regseasoncompactresults['LSeed'] = \
    regseasoncompactresults[['Season','LTeamID']].merge(tourneyseeds,
                                                        left_on = ['Season','LTeamID'],
                                                        right_on = ['Season','TeamID'],
                                                        how='left')[['SeedNumber']]

regseasoncompactresults = \
    regseasoncompactresults.merge(gamecities,
                                  how='left',
                                  on=['Season',
                                      'DayNum',
                                      'WTeamID',
                                      'LTeamID'])

# Add Season Results
regseasoncompactresults = regseasoncompactresults.merge(seasons,
                                                        how='left',
                                                        on='Season')
tourneycompactresults = tourneycompactresults.merge(seasons,
                                                    how='left',
                                                    on='Season')

# Add Team Names
regseasoncompactresults['WTeamName'] = \
    regseasoncompactresults[['WTeamID']].merge(teams,
                                               how='left',
                                               left_on='WTeamID',
                                               right_on='TeamID')[['TeamName']]
regseasoncompactresults['LTeamName'] = \
    regseasoncompactresults[['LTeamID']].merge(teams,
                                               how='left',
                                               left_on='LTeamID',
                                               right_on='TeamID')[['TeamName']]

tourneycompactresults['WTeamName'] = \
    tourneycompactresults[['WTeamID']].merge(teams,
                                             how='left',
                                             left_on='WTeamID',
                                             right_on='TeamID')[['TeamName']]
tourneycompactresults['LTeamName'] = \
    tourneycompactresults[['LTeamID']].merge(teams,
                                             how='left',
                                             left_on='LTeamID',
                                             right_on='TeamID')[['TeamName']]
    
tourneycompactresults['ScoreDiff'] = tourneycompactresults['WScore'] - tourneycompactresults['LScore'] 
