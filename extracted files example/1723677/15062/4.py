GNOISE = 0.25

def make_discriminator():
    image = tf.keras.Input(shape=((64,64,3)))
    label = tf.keras.Input(shape=((1,)))
    x = layers.Embedding(120, 64*64, input_length=1)(label)
    x = layers.Reshape((64,64,1))(x)
    x = layers.concatenate([image,x])
    
    x = layers.Conv2D(MAPS, (5, 5), strides=(2, 2), padding='same', kernel_initializer=init, use_bias=False)(x)
    x = layers.BatchNormalization()(x)
    #x = layers.GaussianNoise(GNOISE)(x)
    x = layers.LeakyReLU()(x)

    x = layers.Conv2D(MAPS*2, (5, 5), strides=(2, 2), padding='same', kernel_initializer=init, use_bias=False)(x)
    x = layers.BatchNormalization()(x)
    #x = layers.GaussianNoise(GNOISE)(x)
    x = layers.LeakyReLU()(x)

    x = layers.Conv2D(MAPS*4, (5, 5), strides=(2, 2), padding='same', kernel_initializer=init, use_bias=False)(x)
    x = layers.BatchNormalization()(x)
    #x = layers.GaussianNoise(GNOISE)(x)
    x = layers.LeakyReLU()(x)

    x = layers.Conv2D(MAPS*8, (5, 5), strides=(2, 2), padding='same', kernel_initializer=init, use_bias=False)(x)
    x = layers.BatchNormalization()(x)
    #x = layers.GaussianNoise(GNOISE)(x)
    x = layers.LeakyReLU()(x)
    
    x = layers.Flatten()(x)
    x = layers.Dense(121, activation='sigmoid')(x)
    x2 = layers.Dense(1, activation='linear')(x)
    
    model = tf.keras.Model(inputs=[image,label], outputs=[x,x2])
    return model

discriminator = make_discriminator()
#discriminator.summary()
