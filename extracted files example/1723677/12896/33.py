# IMPORT LIBRARIES
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation
from sklearn.linear_model import LogisticRegression

# LOAD THE DATA
test = pd.read_csv('../input/test.csv')
train = pd.read_csv('../input/train.csv')
train.head()
