from scipy.cluster.hierarchy import linkage, fcluster

# Get matrix form of the dendrogram 
Z = linkage((sales_ca1>0).astype(int), method='ward')
print(Z)
