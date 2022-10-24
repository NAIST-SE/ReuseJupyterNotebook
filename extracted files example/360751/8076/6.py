# %autosave 600
import numpy as np
import pandas as pd

from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.manifold import TSNE
# from MulticoreTSNE import MulticoreTSNE as TSNE
# %load_ext wurlitzer
