#import data
train = pd.read_csv('../input/avito-demand-prediction/train.csv', usecols = ['city',  'region', 'deal_probability'])
train['location'] = train['city'] + ', ' + train['region']

