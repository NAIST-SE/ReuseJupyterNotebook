pca = PCA(n_components=5) # Selected 5 components just for fun
pca.fit(train[features].as_matrix())

print('The explained variance ratio is {}'.format(pca.explained_variance_ratio_))

pca_components = pd.DataFrame(pca.transform(train[features].as_matrix())) # Create a dataframe with PCA values
pca_components['target'] = train['target'] # Add the target back

# Pairplot of the PCA values vs Target
sns.pairplot(pca_components)
