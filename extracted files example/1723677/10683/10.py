# WRITE SUBMISSION FILE
df_test[['MachineIdentifier','HasDetections']].to_csv('submission.csv', index=False)
