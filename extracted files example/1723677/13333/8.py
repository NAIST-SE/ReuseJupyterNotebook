from keras import applications
#! pip install keras_efficientnets
#from keras_efficientnets import EfficientNetB4

def build_model():
    base_model = applications.Xception(weights='imagenet', input_shape=(350, 525, 3), include_top=False)
    #base_model = EfficientNetB4(input_shape=(350-32, 525-32, 3), include_top=False, weights='imagenet')
    base_model.trainable = False

    x = base_model.output
    x = layers.Flatten()(x)
    x = layers.Dense(256, activation="relu")(x)
    #x = layers.Dropout(0.4)(x)
    x = layers.Dense(256, activation="relu")(x)
    #x = layers.Dropout(0.4)(x)

    pred = layers.Dense(4, activation="linear")(x)
    model = Model(inputs = base_model.input, outputs = pred)
    model.compile(loss='mean_squared_error', optimizer = "adam")
    
    return model
