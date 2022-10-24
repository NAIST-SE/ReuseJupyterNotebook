import numpy as np
import pandas as pd
import missingno as msno

train = pd.read_csv('../input/application_train.csv')
msno.matrix(train.sample(500), inline=True, sparkline=True, figsize=(20,10), sort=None, color=(0.25, 0.45, 0.6))
