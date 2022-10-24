# SUBMIT TO KAGGLE
df_test = pd.read_csv('../input/test.csv', usecols=['MachineIdentifier'])
df_test['HasDetections'] = pred
df_test.to_csv('submission.csv', index=False)
