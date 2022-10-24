test_long['id_seqpos'] = test_long['id'] + '_' + test_long['seqpos'].astype('str')

test_long['deg_pH10'] = 0
test_long['deg_50C'] = 0
test_long = test_long.rename(columns={'reactivity_pred':'reactivity',
                          'deg_Mg_pH10_pred': 'deg_Mg_pH10',
                          'deg_Mg_50C_pred': 'deg_Mg_50C'})

ss = pd.read_csv('../input/stanford-covid-vaccine/sample_submission.csv')
assert test_long[ss.columns].shape == ss.shape

test_long[ss.columns].to_csv('submission.csv', index=False)
