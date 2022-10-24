maxfeats = 5000
word_vectorizer = TfidfVectorizer(
    sublinear_tf=True,
    strip_accents='unicode',
    analyzer='word',
   # token_pattern=r'\w{1,}',
    ngram_range=(1, 1),
    max_features=maxfeats)
word_vectorizer.fit(train_text)
train_features = word_vectorizer.transform(train_text)

classifier = LatentDirichletAllocation(n_components=16, learning_method=None, n_jobs=3, verbose=1)
train_lda = classifier.fit_transform(train_features, train_tgt)
train_lda.shape
