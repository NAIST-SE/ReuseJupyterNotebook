import numpy as np, pandas as pd
load = ['HasDetections', 'AvSigVersion', 'Census_OSVersion', 'OsBuildLab']
df_train = pd.read_csv('../input/microsoft-malware-prediction/train.csv',dtype='category',usecols=load)
df_train['HasDetections'] = df_train['HasDetections'].astype('int8')
