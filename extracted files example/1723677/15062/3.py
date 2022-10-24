MAPS = 128
noise_dim = 128

from tensorflow.keras import layers
from tensorflow.keras.initializers import RandomNormal
init = RandomNormal(mean=0.0, stddev=0.02)

def make_generator():
    seed = tf.keras.Input(shape=((noise_dim,)))
    label = tf.keras.Input(shape=((1,)))
    x = layers.Embedding(120, 120, input_length=1,name='emb')(label)
    x = layers.Flatten()(x)
    x = layers.concatenate([seed,x])
    x = layers.Dense(4*4*MAPS*8, use_bias=False)(x)
    x = layers.Reshape((4, 4, MAPS*8))(x)
    x = layers.BatchNormalization()(x)
    x = layers.ReLU()(x)
    
    x = layers.Conv2DTranspose(MAPS*4, (5, 5), strides=(2, 2), padding='same', kernel_initializer=init, use_bias=False)(x)
    x = layers.BatchNormalization()(x)
    x = layers.ReLU()(x)
    
    x = layers.Conv2DTranspose(MAPS*2, (5, 5), strides=(2, 2), padding='same', kernel_initializer=init, use_bias=False)(x)
    x = layers.BatchNormalization()(x)
    x = layers.ReLU()(x)
    
    x = layers.Conv2DTranspose(MAPS, (5, 5), strides=(2, 2), padding='same', kernel_initializer=init, use_bias=False)(x)
    x = layers.BatchNormalization()(x)
    x = layers.ReLU()(x)
    
    x = layers.Conv2DTranspose(3, (5, 5), strides=(2, 2), padding='same', kernel_initializer=init, use_bias=False, activation='tanh')(x)

    model = tf.keras.Model(inputs=[seed,label], outputs=x)    
    return model

generator = make_generator()
#generator.summary()
