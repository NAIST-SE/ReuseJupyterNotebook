train = pd.read_csv('../input/osic-pulmonary-fibrosis-progression/train.csv')
train = train.query('Sex=="Male" & Age>60')
train.SmokingStatus.value_counts(normalize=True)
