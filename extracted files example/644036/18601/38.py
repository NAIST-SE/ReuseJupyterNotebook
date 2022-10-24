MEvents['PointsScored'] =  0
MEvents.loc[MEvents['EventType'] == 'made2', 'PointsScored'] = 2
MEvents.loc[MEvents['EventType'] == 'made3', 'PointsScored'] = 3
MEvents.loc[MEvents['EventType'] == 'missed2', 'PointsScored'] = 0
MEvents.loc[MEvents['EventType'] == 'missed3', 'PointsScored'] = 0
