# Use the Maximum frame predicted as "Fake" to be the final prediction
ss['label'] = ss['max_pred'].fillna(0.5).clip(0.4, 0.8)
