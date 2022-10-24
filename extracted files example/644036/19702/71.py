import lightgbm as lgb
pd.set_option('max_columns', 500)
try:
    tt['healthexp'] = pd.to_numeric(tt['healthexp'].str.replace(',',''))
except:
    pass
train = tt.loc[tt['Date'] < '25-March-2020']
test = tt.loc[tt['Date'] >= '25-March-2020']
