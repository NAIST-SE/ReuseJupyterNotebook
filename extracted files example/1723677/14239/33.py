for clusters in range(4):
    centers = np.array([])
    for k in range(512):
        X, y = make_classification(n_samples=768, n_features=useful[k], 
                    n_informative=useful[k], n_redundant=0, n_repeated=0, 
                    n_classes=2, n_clusters_per_class=clusters+1, weights=None, 
                    flip_y=0.05, class_sep=1.0, hypercube=True, shift=0.0, scale=1.0, 
                    shuffle=True, random_state=None)
        centers = np.append(centers,np.mean(X[ np.argwhere(y==0).flatten() ,:],axis=0))
        centers = np.append(centers,np.mean(X[ np.argwhere(y==1).flatten() ,:],axis=0))
    plt.hist(centers,bins=100)
    plt.title('Variable means if clusters='+str(clusters+1))
    plt.show()
