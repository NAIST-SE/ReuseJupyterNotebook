#%% import
import time
import numpy as np
import pandas as pd
import spacy as sp
nlp_lg = sp.load('en_core_web_lg')
from sklearn.model_selection import StratifiedKFold, train_test_split
from sklearn.metrics import f1_score
from sklearn.linear_model import LogisticRegression
from tqdm import tqdm


# get train data
train = pd.read_csv('../input/train.csv', nrows=30_000)  #limiting the data for time's sake
train['question_text'] = train.question_text.str.replace('?', ' ?')
train['question_text'] = train.question_text.str.replace('.', ' .')
