from scipy.cluster.hierarchy import fcluster

def print_clusters(deviation_pivot, Z, k, plot=False):
    # k Number of clusters I'd like to extract
    results = fcluster(Z, k, criterion='maxclust')

    # check the results
    s = pd.Series(results)
    clusters = s.unique()

    for c in clusters:
        cluster_indeces = s[s==c].index
        print("Cluster %d number of entries %d" % (c, len(cluster_indeces)))
        if plot:
            deviation_pivot.T.iloc[:,cluster_indeces].plot()
            plt.show()

print_clusters(deviation_pivot, Z, 5, plot=False)
