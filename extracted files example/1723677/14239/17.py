if np.allclose(useful_train,useful_public):
    print('Public dataset has the SAME structure as train')
else:
    print('Public dataset DOES NOT HAVE the same structure as train')
