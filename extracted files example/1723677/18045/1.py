import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
from scipy.stats import mode
from sklearn.metrics import f1_score, accuracy_score
from cuml.neighbors import KNeighborsClassifier, NearestNeighbors
import cuml; cuml.__version__
