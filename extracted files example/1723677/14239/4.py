from sklearn.model_selection import StratifiedKFold
from sklearn import metrics, preprocessing

import tensorflow as tf
tf.logging.set_verbosity(tf.logging.ERROR) #hide warnings
from keras.layers import Dense, Input
from keras.layers import BatchNormalization
from keras.models import Model
from keras import callbacks
from keras import backend as K
from keras.layers import Dropout
from keras.callbacks import LearningRateScheduler

import warnings
warnings.filterwarnings("ignore")
