####
#train_lda = train_features.toarray()

tsne = TSNE(n_components=2, perplexity=8, n_iter=1600, verbose=1, angle=0.5)
train_tsne = tsne.fit_transform(train_lda)
x_tsne = train_tsne[:, 0]
y_tsne = train_tsne[:, 1]
