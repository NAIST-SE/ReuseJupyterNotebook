ss['isFraud'] = test_preds
ss.to_csv('predictions.csv', index=False)
