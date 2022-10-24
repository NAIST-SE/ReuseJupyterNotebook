train = pd.read_csv('../input/train.csv', dtype={'fullVisitorId': str, 'date': str}, parse_dates=['date'],
        index_col=('fullVisitorId', 'sessionId'))
train.head()
