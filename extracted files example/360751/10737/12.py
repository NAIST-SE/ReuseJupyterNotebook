%%time
#%% get libraries and data
import os
import re
import string
import numpy as np 
import pandas as pd
from scipy.sparse import csr_matrix, hstack
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import StratifiedKFold, train_test_split
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score, roc_auc_score

numrows = None
train = pd.read_csv('../input/train.csv', index_col=['qid'], nrows=numrows)
test = pd.read_csv('../input/test.csv', index_col=['qid'], nrows=numrows)
y = train.target.values

#%% make word vectors - todo:catch numbers and punctuation, find faster tokenizer (NTLK, Spacy?)
word_vectorizer = TfidfVectorizer(ngram_range=(1,2),
                                    min_df=3,
                                    max_df=0.9,
                                    token_pattern=r'\w{1,}',
                                    stop_words='english',
                                    max_features=50_000,
                                    strip_accents='unicode',
                                    use_idf=True,
                                    smooth_idf=True,
                                    sublinear_tf=True)

print("tokenizing")
word_vectorizer.fit(pd.concat((train['question_text'], test['question_text'])))
X = word_vectorizer.transform(train['question_text'])
X_test = word_vectorizer.transform(test['question_text'])

#%% make character vectors - coming soon


