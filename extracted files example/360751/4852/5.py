# Map items to clusters
clust = fcluster(Z, t=12, criterion='maxclust')
pd.crosstab(clust, sales_ca1.index.str[:-6])
