import pandas as pd
import numpy as np
import json
from tqdm.notebook import tqdm
from sklearn.model_selection import train_test_split
import lightgbm as lgb
import matplotlib.pylab as plt

def expand_columns(df):
    df = df.copy()
    df = df.drop('index', axis=1)
    max_seq_length = df['seq_length'].max()
    SEQUENCE_COLS = []; STRUCTURE_COLS = []; PRED_LOOP_TYPE_COLS = []
    for s in range(130):
        df[f'sequence_{s}'] = df['sequence'].str[s]
        df[f'structure_{s}'] = df['structure'].str[s]
        df[f'predicted_loop_type_{s}'] = df['predicted_loop_type'].str[s]
        SEQUENCE_COLS.append(f'sequence_{s}')
        STRUCTURE_COLS.append(f'structure_{s}')
    return df, SEQUENCE_COLS, STRUCTURE_COLS

def parse_sample_submission(ss):
    ss = ss.copy()
    ss['id'] = ss['id_seqpos'].str.split('_', expand=True)[1]
    ss['seqpos'] = ss['id_seqpos'].str.split('_', expand=True)[2].astype('int')
    return ss
