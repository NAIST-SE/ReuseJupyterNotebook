# Area Mapping Names
area_mapping = {0: np.nan,
                1: 'under basket',
                2: 'in the paint',
                3: 'inside right wing',
                4: 'inside right',
                5: 'inside center',
                6: 'inside left',
                7: 'inside left wing',
                8: 'outside right wing',
                9: 'outside right',
                10: 'outside center',
                11: 'outside left',
                12: 'outside left wing',
                13: 'backcourt'}

MEvents['Area_Name'] = MEvents['Area'].map(area_mapping)
WEvents['Area_Name'] = WEvents['Area'].map(area_mapping)

# Normalize X, Y positions for court dimentions
# Court is 50 feet wide and 94 feet end to end.
MEvents['X_'] = (MEvents['X'] * (94/100))
MEvents['Y_'] = (MEvents['Y'] * (50/100))

WEvents['X_'] = (WEvents['X'] * (94/100))
WEvents['Y_'] = (WEvents['Y'] * (50/100))


# Create Half Court X/Y Features for Plotting
# Mens
MEvents['X_half'] = MEvents['X']
MEvents.loc[MEvents['X'] > 50, 'X_half'] = (100 - MEvents['X'].loc[MEvents['X'] > 50])
MEvents['Y_half'] = MEvents['Y']
MEvents.loc[MEvents['X'] > 50, 'Y_half'] = (100 - MEvents['Y'].loc[MEvents['X'] > 50])

MEvents['X_half_'] = (MEvents['X_half'] * (94/100))
MEvents['Y_half_'] = (MEvents['Y_half'] * (50/100))

# Womens
WEvents['X_half'] = WEvents['X']
WEvents.loc[WEvents['X'] > 50, 'X_half'] = (100 - WEvents['X'].loc[WEvents['X'] > 50])
WEvents['Y_half'] = WEvents['Y']
WEvents.loc[WEvents['X'] > 50, 'Y_half'] = (100 - WEvents['Y'].loc[WEvents['X'] > 50])

WEvents['X_half_'] = (WEvents['X_half'] * (94/100))
WEvents['Y_half_'] = (WEvents['Y_half'] * (50/100))

# Add Player Info
MEvents = MEvents.merge(MPlayers,
                        how='left',
                        left_on=['EventPlayerID'],
                        right_on='PlayerID')

WEvents = WEvents.merge(MPlayers,
                        how='left',
                        left_on=['EventPlayerID'],
                        right_on='PlayerID')
