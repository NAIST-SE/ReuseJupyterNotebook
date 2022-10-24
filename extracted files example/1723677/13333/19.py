# USE KERAS XCEPTION MODEL
from keras.applications.xception import Xception
base_model = Xception(weights='imagenet',include_top=False,input_shape=(None,None,3))
# FREEZE NON-BATCHNORM LAYERS IN BASE
for layer in base_model.layers:
    if not isinstance(layer, layers.BatchNormalization): layer.trainable = False
# BUILD MODEL NEW TOP
x = base_model.output
x = layers.GlobalAveragePooling2D()(x)
x = layers.Dense(4,activation='sigmoid')(x)
model = Model(inputs=base_model.input, outputs=x)
# COMPILE MODEL
model.compile(loss='binary_crossentropy', optimizer = optimizers.Adam(lr=0.001), metrics=['accuracy'])

# SPLIT TRAIN AND VALIDATE
idxT, idxV = train_test_split(train2.index, random_state=42, test_size=0.2)
train_gen = DataGenerator(idxT, flips=True, shuffle=True)
val_gen = DataGenerator(idxV, mode='validate')

# TRAIN NEW MODEL TOP LR=0.001 (with bottom frozen)
h = model.fit_generator(train_gen, epochs = 2, verbose=2, validation_data = val_gen)
# TRAIN ENTIRE MODEL LR=0.0001 (with all unfrozen)
for layer in model.layers: layer.trainable = True
model.compile(loss='binary_crossentropy', optimizer = optimizers.Adam(lr=0.0001), metrics=['accuracy'])
h = model.fit_generator(train_gen, epochs = 2, verbose=2, validation_data = val_gen)
