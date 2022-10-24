# PREDICT IN CHUNKS FOR REDUCED MEMORY USAGE
idx = 0; chunk = 2000000
pred_val = np.zeros(len(df_test))
while idx < len(df_test):
    idx2 = min(idx + chunk, len(df_test) )
    idx = range(idx, idx2)
    pred_val[idx] = model.predict_proba(df_test.iloc[idx])[:,1]
    idx = idx2
submit = pd.read_csv('../input/microsoft-malware-prediction/sample_submission.csv')
submit['HasDetections'] = pred_val
submit.to_csv('ExternalData.csv', index=False)
