top_10_defenses = train.groupby('DefensePersonnel')['GameId'] \
    .count() \
    .sort_values(ascending=False).index[:10] \
    .tolist()
