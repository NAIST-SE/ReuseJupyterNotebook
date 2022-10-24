# Example from here:
# https://stackoverflow.com/questions/34940808/hierarchical-clustering-of-time-series-in-python-scipy-numpy-pandas
    
import scipy.cluster.hierarchy as hac
from scipy import stats
# Here we use spearman correlation
def my_metric(x, y):
    r = stats.pearsonr(x, y)[0]
    return 1 - r # correlation to distance: range 0 to 2

Z = hac.linkage(deviation_pivot, method='single', metric=my_metric)
