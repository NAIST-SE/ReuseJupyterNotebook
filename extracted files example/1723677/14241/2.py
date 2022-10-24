from keras import applications
base_model = applications.Xception(weights=None, input_shape=(256, 256, 3), include_top=False)
base_model.load_weights('../input/keras-pretrained-models/xception_weights_tf_dim_ordering_tf_kernels_notop.h5')
base_model.trainable = False
x = base_model.output
x = layers.Flatten()(x)
x = layers.Dense(1024, activation="relu")(x)
x = layers.Dropout(0.5)(x)
predictions = layers.Dense(1, activation="sigmoid")(x)
model = Model(input = base_model.input, output = predictions)
model.compile(loss='binary_crossentropy', optimizer = "adam", metrics=['accuracy'])
