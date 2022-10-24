import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pylab as plt
import seaborn as sns

train = pd.read_csv('../input/ashrae-energy-prediction/train.csv')
test = pd.read_csv('../input/ashrae-energy-prediction/test.csv')
weather_te = pd.read_csv('../input/ashrae-energy-prediction/weather_test.csv')
weather_tr = pd.read_csv('../input/ashrae-energy-prediction/weather_train.csv')
bmd = pd.read_csv('../input/ashrae-energy-prediction/building_metadata.csv')

# Set timestamps
train['timestamp'] = pd.to_datetime(train['timestamp'])
test['timestamp'] = pd.to_datetime(test['timestamp'])
weather_tr['timestamp'] = pd.to_datetime(weather_tr['timestamp'])
weather_te['timestamp'] = pd.to_datetime(weather_te['timestamp'])

sns.set(style="whitegrid")
sns.set_color_codes("pastel")
