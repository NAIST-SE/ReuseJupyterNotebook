# Lower detection rate for August and September computers
AdjustPublicScore = True
# 0=No, 1=Remove Nov 20,21,22,23,24,25, 2=Downward trend Nov 20,21,22,23,24,25
AdjustPrivateScore = 2

dtypes = {}
dtypes['MachineIdentifier'] = 'str'
dtypes['AvSigVersion'] = 'category'
dtypes['HasDetections'] = 'int8'

# LOAD TRAIN DATA
df_train = pd.read_csv('../input/microsoft-malware-prediction/train.csv', usecols=list(dtypes.keys()), dtype=dtypes)
print ('Loaded',len(df_train),'rows of train.CSV!')

# LOAD TEST DATA
df_test = pd.read_csv('../input/microsoft-malware-prediction/test.csv', usecols=list(dtypes.keys())[0:-1], dtype=dtypes)
print ('Loaded',len(df_test),'rows of test.CSV!')

# LOAD PREDICTIONS FROM PUBLIC KERNEL
# https://www.kaggle.com/hung96ad/new-blend
df_test2 = pd.read_csv('../input/kagglebest/super_blend.csv')
print ('Loaded',len(df_test),'rows of super_blend.csv!')

# ADD TIMESTAMPS
datedictAS = np.load('../input/malware-timestamps/AvSigVersionTimestamps.npy')[()]
df_test['Date'] = df_test['AvSigVersion'].map(datedictAS)
df_train['Date'] = df_train['AvSigVersion'].map(datedictAS)
df_test2 = pd.merge(df_test2, df_test, on='MachineIdentifier', how='left')
df_test2['AvSigVersion2'] = df_test2['AvSigVersion'].map(lambda x: np.int(x.split('.')[1]) )
