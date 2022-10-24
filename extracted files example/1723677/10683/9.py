del df_train; x=gc.collect()
df_test = pd.read_csv('../input/microsoft-malware-prediction/test.csv',
            usecols=['MachineIdentifier','AvSigVersion'], nrows=len(pred_val))

# CORRECT PREDICTIONS FOR OUTLIERS IN PRIVATE TEST DATASET
from datetime import datetime
datedictAS = np.load('../input/malware-timestamps/AvSigVersionTimestamps.npy')[()]
df_test['Date'] = df_test['AvSigVersion'].map(datedictAS)
df_test['HasDetections'] = pred_val / 5.0
df_test['X'] = df_test['Date'] - datetime(2018,11,20,4,0) 
df_test['X'] = df_test['X'].map(lambda x: x.total_seconds()/86400)
df_test['X'].fillna(0,inplace=True)
s = 5.813888
df_test['F'] = 1.0
df_test['F'] = 1 - df_test['X']/s
df_test.loc[df_test['X']<=0,'F'] = 1.0
df_test.loc[df_test['X']>s,'F'] = 0
df_test['HasDetections'] *= df_test['F']
