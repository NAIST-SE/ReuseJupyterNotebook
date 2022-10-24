import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os
import matplotlib.pylab as plt
import plotly
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from sklearn.linear_model import LinearRegression
import datetime
import colorlover as cl
plt.style.use('ggplot')
color_pal = [x['color'] for x in plt.rcParams['axes.prop_cycle']]

# Format the dataa
df = pd.read_csv('../input/molecular-properties-leaderboard/champs-scalar-coupling-publicleaderboard_08_28_2019.csv')
df['SubmissionDate'] = pd.to_datetime(df['SubmissionDate'])
df = df.set_index(['TeamName','SubmissionDate'])['Score'].unstack(-1).T
df.columns = [name for name in df.columns]

FIFTEENTH_SCORE = df.min().sort_values(ascending=True)[15]
FIFTYTH_SCORE = df.min().sort_values(ascending=True)[50]
TOP_SCORE = df.min().sort_values(ascending=True)[0]
