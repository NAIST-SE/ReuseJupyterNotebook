import tensorflow as tf
tf.enable_eager_execution()

# FUNCTION FOR DATA AUGMENTATION
def flip(x: tf.Tensor, y:tf.Tensor) -> (tf.Tensor,tf.Tensor):
    x = tf.image.random_flip_left_right(x)
    return (x,y)

# FUNCTION FOR DATA AUGMENTATION
def crop(x: tf.Tensor, y:tf.Tensor) -> (tf.Tensor,tf.Tensor):
    x = tf.random_crop(x,size=[64,64,3])
    return (x,y)
