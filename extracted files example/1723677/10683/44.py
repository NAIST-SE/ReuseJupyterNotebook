import numpy as np, pandas as pd, gc, random
import matplotlib.pyplot as plt

def load(x):
    ignore = ['MachineIdentifier']
    if x in ignore: return False
    else: return True

# LOAD TRAIN AND TEST
df_train = pd.read_csv('../input/microsoft-malware-prediction/train.csv',dtype='category',usecols=load)
df_train['HasDetections'] = df_train['HasDetections'].astype('int8')
if 5244810 in df_train.index:
    df_train.loc[5244810,'AvSigVersion'] = '1.273.1144.0'
    df_train['AvSigVersion'].cat.remove_categories('1.2&#x17;3.1144.0',inplace=True)
#df_train = df_train.sample(8000000).reset_index(drop=True)

df_test = pd.read_csv('../input/microsoft-malware-prediction/test.csv',dtype='category',usecols=load)
#df_test = df_test.sample(1000000).reset_index(drop=True)
