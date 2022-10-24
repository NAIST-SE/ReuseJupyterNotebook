import numpy as np, pandas as pd
train = pd.read_csv('../input/train.csv')
train0 = train[ train['target']==0 ].copy()
train1 = train[ train['target']==1 ].copy()
train.sample(5)
