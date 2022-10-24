from sklearn.preprocessing import StandardScaler

ss = StandardScaler()
scaled = ss.fit_transform(train[['var_{}'.format(x) for x in range(0, 200)]])

scaleddf = pd.DataFrame(scaled)
scaleddf_T = scaleddf.T
