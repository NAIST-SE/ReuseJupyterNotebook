%%timeit
# This block is SPED UP a little more

train_p_0 = train[['x_0', 'y_0', 'z_0']].values
train_p_1 = train[['x_1', 'y_1', 'z_1']].values
test_p_0 = test[['x_0', 'y_0', 'z_0']].values
test_p_1 = test[['x_1', 'y_1', 'z_1']].values

tr_a_min_b = train_p_0 - train_p_1
te_a_min_b = test_p_0 - test_p_1
train['dist_speedup_einsum'] = np.sqrt(np.einsum('ij,ij->i', tr_a_min_b, tr_a_min_b))
test['dist_speedup_einsum'] = np.sqrt(np.einsum('ij,ij->i', te_a_min_b, te_a_min_b))
