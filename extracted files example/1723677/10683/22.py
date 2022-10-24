from datetime import datetime, date, timedelta

# AS timestamp
datedictAS = np.load('../input/malware-timestamps/AvSigVersionTimestamps.npy')[()]
df_train['DateAS'] = df_train['AvSigVersion'].map(datedictAS)  

# OS timestamp
datedictOS = np.load('../input/malware-timestamps-2/OSVersionTimestamps.npy')[()]
df_train['DateOS'] = df_train['Census_OSVersion'].map(datedictOS)  

# BL timestamp
def convert(x):
    try:
        d = datetime.strptime(x.split('.')[4],'%y%m%d-%H%M')
    except:
        d = np.nan
    return d
df_train['DateBL'] = df_train['OsBuildLab'].map(convert)
df_train.head()
