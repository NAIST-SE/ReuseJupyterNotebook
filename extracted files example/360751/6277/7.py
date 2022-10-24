# create a lookup table from train
q1s = train.iloc[:, [1,3]]
q2s = train.iloc[:, [2,4]]

new_cols = ['qid', 'question']
q1s.columns = new_cols
q2s.columns = new_cols

lookup = pd.concat([q1s, q2s], ignore_index=True)
lookup.drop_duplicates('qid', inplace=True)
