print('Writing submission file...')
if Debug:
    submit = pd.read_csv('../input/microsoft-malware-prediction/sample_submission.csv', nrows=10000)
else:
    submit = pd.read_csv('../input/microsoft-malware-prediction/sample_submission.csv')
submit['HasDetections'] = pred
submit.to_csv('submission.csv', index=False)
print('Done!')
