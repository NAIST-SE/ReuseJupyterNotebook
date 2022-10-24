import numpy as np, pandas as pd, os
np.random.seed(300)

# GENERATE USELESS VARIABLES AND RANDOM TARGETS
train = pd.DataFrame(np.zeros((250,300)))
for i in range(300): train.iloc[:,i] = np.random.normal(0,1,250)
train['target'] = np.random.uniform(0,1,250)
train.loc[ train['target']>0.34, 'target'] = 1.0
train.loc[ train['target']<=0.34, 'target'] = 0.0
