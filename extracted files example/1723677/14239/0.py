import numpy as np, pandas as pd, os, gc

train = pd.read_csv('../input/train.csv')
test = pd.read_csv('../input/test.csv')

train.head()
