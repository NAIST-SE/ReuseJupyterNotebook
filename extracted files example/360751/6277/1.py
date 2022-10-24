trainstay = train.loc[train['is_duplicate'] == 1, ['qid1', 'qid2']]
stays = pd.Series(trainstay.values.ravel()).unique().tolist()
allvals = list(range(1, 537934)) # one larger than our max qid
solos = set(allvals) - set (stays)
print(len(solos))
print(max(allvals))
