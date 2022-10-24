import time
kernel_start = time.time()
LIMIT = 8.8

DO_TRAIN = True
DO_TEST = True
USE_TTA = True

RAND = 12345

!pip install tensorflow-gpu==1.14.0 --quiet
!pip install keras==2.2.4 --quiet
!pip install segmentation-models --quiet

import albumentations as albu
import cv2, gc, os
import keras
from keras import backend as K
from keras.models import Model
from keras.layers import Input
from keras import layers
from keras.layers.convolutional import Conv2D, Conv2DTranspose
from keras.layers.pooling import MaxPooling2D
from keras.layers.merge import concatenate
from keras.losses import binary_crossentropy
from keras.callbacks import Callback, ModelCheckpoint, EarlyStopping, ReduceLROnPlateau
from skimage.exposure import adjust_gamma
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from tqdm import tqdm
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from keras.models import load_model
import segmentation_models as sm
from sklearn.metrics import roc_auc_score, accuracy_score

import keras.backend as K
from keras.legacy import interfaces
from keras.optimizers import Optimizer
