!pip install tensorflow-gpu==1.14.0 --quiet
!pip install keras==2.2.4 --quiet

import keras
import numpy as np, pandas as pd, os 
from keras import layers
from keras.models import Model
from PIL import Image
from keras import optimizers
import scipy, cv2   
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, accuracy_score
