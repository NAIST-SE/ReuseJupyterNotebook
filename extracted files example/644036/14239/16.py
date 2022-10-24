train_df = pd.read_csv('../input/train.csv')
test_df = pd.read_csv('../input/test.csv')

y_train = train_df['target'].copy()
id_train = train_df['id'].copy()
X_train = train_df.drop(['target', 'id'], axis=1)
id_text = test_df['id'].copy()
X_test = test_df.drop(['id'], axis=1)
