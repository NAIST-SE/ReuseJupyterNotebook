# SET THIS VARIABLE TO TRUE TO RUN KERNEL QUICKLY AND FIND BUGS
# ONLY 10000 ROWS OF DATA IS LOADED
Debug = False

import numpy as np, pandas as pd, gc, random
import matplotlib.pyplot as plt

def load(x):
    ignore = ['MachineIdentifier']
    if x in ignore: return False
    else: return True

# LOAD TRAIN AND TEST
if Debug:
    df_train = pd.read_csv('../input/microsoft-malware-prediction/train.csv',dtype='category',usecols=load,nrows=10000)
else:
    df_train = pd.read_csv('../input/microsoft-malware-prediction/train.csv',dtype='category',usecols=load)
df_train['HasDetections'] = df_train['HasDetections'].astype('int8')
if 5244810 in df_train.index:
    df_train.loc[5244810,'AvSigVersion'] = '1.273.1144.0'
    df_train['AvSigVersion'].cat.remove_categories('1.2&#x17;3.1144.0',inplace=True)

if Debug:
    df_test = pd.read_csv('../input/microsoft-malware-prediction/test.csv',dtype='category',usecols=load,nrows=10000)
else:
    df_test = pd.read_csv('../input/microsoft-malware-prediction/test.csv',dtype='category',usecols=load)
    
print('Loaded',len(df_train),'rows of TRAIN and',len(df_test),'rows of TEST')
