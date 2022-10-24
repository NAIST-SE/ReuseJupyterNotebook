# ONE-HOT-ENCODE THE MAGIC FEATURE
len_train = train.shape[0]
test['target'] = -1
data = pd.concat([train, test])
data = pd.concat([data, pd.get_dummies(data['wheezy-copper-turtle-magic'])], axis=1, sort=False)

train = data[:len_train]
test = data[len_train:]
