cols2 = {'AVProductStatesIdentifier':0.01, 'CountryIdentifier':0.4, 'LocaleEnglishNameIdentifier':0.3, 'SmartScreen':0.4,
         'Census_OEMNameIdentifier':0.1,'Census_TotalPhysicalRAM':0.5,'Census_InternalPrimaryDiagonalDisplaySizeInInches':0.05,
        'Census_OSInstallTypeName':0.75,'Census_OSInstallLanguageIdentifier':0.3,'Census_FirmwareManufacturerIdentifier':0.1,
        'EngineVersion':1.0, 'AppVersion':0.7, 'OsBuildLab':0.2, 'Census_OEMModelIdentifier':0.15,
        'Census_InternalBatteryNumberOfCharges':0.05}

df_train = pd.read_csv('../input/microsoft-malware-prediction/train.csv',dtype='category',usecols=load)
df_test = pd.read_csv('../input/microsoft-malware-prediction/test.csv',dtype='category',usecols=load)
df_test['DateAS'] = df_test['AvSigVersion'].map(datedictAS)
df_testA = df_test[ df_test['DateAS']<datetime(2018,10,25) ]
df_testB = df_test[ df_test['DateAS']>datetime(2018,10,25) ]

for x in df_train.columns[:-2]:
    s = 0.5
    if x in cols2: s = cols2[x] 
    comparePlot(df_train,df_testA,x,scale=s, title='Public Test vs. Train', prefix='Public ')
    comparePlot(df_train,df_testB,x,scale=s, title='Private Test vs. Train', prefix='Private ')
