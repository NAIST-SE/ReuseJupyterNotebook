train = pd.read_csv('../input/data-without-drift/train_clean.csv')
test = pd.read_csv('../input/data-without-drift/test_clean.csv')
tt = pd.concat([train, test], sort=False)
