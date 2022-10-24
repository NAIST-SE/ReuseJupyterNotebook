card_cols = [c for c in train_transaction.columns if 'card' in c]
train_transaction[card_cols].head()
