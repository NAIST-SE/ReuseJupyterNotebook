import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


targets_treated = targets.drop(targets_0_idx)
corr_mtx = abs(targets_treated.corr())

corr_map = corr_mtx[corr_mtx>=.7]
plt.figure(figsize=(12,8))
sns.heatmap(corr_map, cmap="viridis")
