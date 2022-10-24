import numpy as np, pandas as pd, os
np.random.seed(300)

# GENERATE RANDOM DATA
data = pd.DataFrame(np.zeros((20000,300)))
for i in range(300): data.iloc[:,i] = np.random.normal(0,1,20000)

# SET TARGET AS LINEAR COMBINATION OF 50 A'S PLUS NOISE 
important = 35; noise = 3.5
a = np.random.normal(0,1,300)
x = np.random.choice(np.arange(300),300-important,replace=False); a[x] = 0
data['target'] = data.values.dot(a) + np.random.normal(0,noise,20000)

# MAKE 64% TARGET=1, 36% TARGET=0
data.sort_values('target',inplace=True)
data.iloc[:7200,300] = 0.0
data.iloc[7200:,300] = 1.0

# RANDOMLY SELECT TRAIN, PUBLIC, PRIVATE
train = data.sample(250)
public = data[ ~data.index.isin(train.index) ].sample(1975)
private = data[ ~data.index.isin(train.index) & ~data.index.isin(public.index) ].sample(frac=1) 

# RESET INDICES
train.reset_index(drop=True,inplace=True)
public.reset_index(drop=True,inplace=True)
private.reset_index(drop=True,inplace=True)
