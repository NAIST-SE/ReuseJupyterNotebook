from datetime import datetime, date, timedelta

# AS timestamp
datedictAS = np.load('../input/malware-timestamps/AvSigVersionTimestamps.npy')[()]
df_train['DateAS'] = df_train['AvSigVersion'].map(datedictAS)
df_test['DateAS'] = df_test['AvSigVersion'].map(datedictAS)

# OS timestamp
datedictOS = np.load('../input/malware-timestamps-2/OSVersionTimestamps.npy')[()]
df_train['DateOS'] = df_train['Census_OSVersion'].map(datedictOS)
df_test['DateOS'] = df_test['Census_OSVersion'].map(datedictOS)

# ENGINEERED FEATURE #1
df_train['AppVersion2'] = df_train['AppVersion'].map(lambda x: np.int(x.split('.')[1]))
df_test['AppVersion2'] = df_test['AppVersion'].map(lambda x: np.int(x.split('.')[1]))

# ENGINEERED FEATURE #2
df_train['Lag1'] = df_train['DateAS'] - df_train['DateOS']
df_train['Lag1'] = df_train['Lag1'].map(lambda x: x.days//7)
df_test['Lag1'] = df_test['DateAS'] - df_test['DateOS']
df_test['Lag1'] = df_test['Lag1'].map(lambda x: x.days//7)

# ENGINEERED FEATURE #3
df_train['Lag5'] = datetime(2018,7,26) - df_train['DateAS']
df_train['Lag5'] = df_train['Lag5'].map(lambda x: x.days//1)
df_train.loc[ df_train['Lag5']<0, 'Lag5' ] = 0
df_test['Lag5'] = datetime(2018,9,27) - df_test['DateAS'] #PUBLIC TEST
df_test['Lag5'] = df_test['Lag5'].map(lambda x: x.days//1)
df_test.loc[ df_test['Lag5']<0, 'Lag5' ] = 0
df_train['Lag5'] = df_train['Lag5'].astype('float32') # allow for NAN
df_test['Lag5'] = df_test['Lag5'].astype('float32') # allow for NAN

# ENGINEERED FEATURE #4
df_train['driveA'] = df_train['Census_SystemVolumeTotalCapacity'].astype('float')/df_train['Census_PrimaryDiskTotalCapacity'].astype('float')
df_test['driveA'] = df_test['Census_SystemVolumeTotalCapacity'].astype('float')/df_test['Census_PrimaryDiskTotalCapacity'].astype('float')
df_train['driveA'] = df_train['driveA'].astype('float32') 
df_test['driveA'] = df_test['driveA'].astype('float32') 

# ENGINNERED FEATURE #5
df_train['driveB'] = df_train['Census_PrimaryDiskTotalCapacity'].astype('float') - df_train['Census_SystemVolumeTotalCapacity'].astype('float')
df_test['driveB'] = df_test['Census_PrimaryDiskTotalCapacity'].astype('float') - df_test['Census_SystemVolumeTotalCapacity'].astype('float')
df_train['driveB'] = df_train['driveB'].astype('float32') 
df_test['driveB'] = df_test['driveB'].astype('float32') 

cols6=['Lag1']
cols8=['Lag5','driveB','driveA']

del df_train['DateAS'], df_train['DateOS'] #, df_train['DateBL']
del df_test['DateAS'], df_test['DateOS'] #, df_test['DateBL']
del datedictAS, datedictOS
x=gc.collect()
