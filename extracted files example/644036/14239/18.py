# This feature is more categorical than continious
train_df['wheezy-copper-turtle-magic'] = train_df['wheezy-copper-turtle-magic'].astype('category')
test_df['wheezy-copper-turtle-magic'] = test_df['wheezy-copper-turtle-magic'].astype('category')
X_train['wheezy-copper-turtle-magic'] = X_train['wheezy-copper-turtle-magic'].astype('category')
X_test['wheezy-copper-turtle-magic'] = X_test['wheezy-copper-turtle-magic'].astype('category')
