%%time

perm = PermutationImportance(rf_model, scoring=scorer, cv=skf)
perm.fit(X, y)
