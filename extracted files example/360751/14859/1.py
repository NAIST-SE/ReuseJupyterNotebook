train = pd.read_csv('/kaggle/input/bigquery-geotab-intersection-congestion/train.csv', 
                    index_col='RowId')
test = pd.read_csv('/kaggle/input/bigquery-geotab-intersection-congestion/test.csv', 
                    index_col='RowId')
target_cols = [col for col in train.columns.tolist() if
                    col not in test.columns.tolist()]
target_df = train[(target_cols)]
train = train.drop(target_cols, axis=1)
