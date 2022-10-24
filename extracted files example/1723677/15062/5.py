# THESE LOSS FUNCTIONS ARE UNUSED. THEY ARE REWRITTEN INSIDE TRAINING LOOP BELOW
from tensorflow.contrib.eager.python import tfe

# RaLS Discriminator Loss
def RaLS_errD(fake,real):
    return (tf.reduce_mean( (real - tf.reduce_mean(fake,0) - tf.ones_like(real))**2,0 )
        + tf.reduce_mean( (fake - tf.reduce_mean(real,0) + tf.ones_like(real))**2,0 ) )/2.

# RaLS Generator Loss
def RaLS_errG(fake,real):
    return (tf.reduce_mean( (real - tf.reduce_mean(fake,0) + tf.ones_like(real))**2,0 )
        + tf.reduce_mean( (fake - tf.reduce_mean(real,0) - tf.ones_like(real))**2,0 ) )/2.

# OPTIMIZER - ADAM
learning_rate = tfe.Variable(0.0002)
generator_optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate, beta1=0.5)
discriminator_optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate, beta1=0.5)
