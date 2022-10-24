BATCH_SIZE = 32

from sklearn import preprocessing

for i in range(len(namesIn)):
    namesIn[i] = namesIn[i].split('-')[1].lower()
le = preprocessing.LabelEncoder()
namesIn = le.fit_transform(namesIn)

imagesIn = (imagesIn[:idxIn,:,:,:]-127.5)/127.5
namesIn = namesIn[:idxIn]
imagesIn = imagesIn.astype('float32')
namesIn = namesIn.astype('int8')
ds = tf.data.Dataset.from_tensor_slices((imagesIn,namesIn)).map(flip).map(crop).batch(BATCH_SIZE,drop_remainder=True)
print('TF Version',tf.__version__); print()
print('Our TF data pipeline has been built')
print(ds)
