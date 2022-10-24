# INITIALIZE VARIABLES
IMAGE_SIZE= [512,512]; BATCH_SIZE = 32
AUTO = tf.data.experimental.AUTOTUNE
TRAINING_FILENAMES = tf.io.gfile.glob('train*.tfrec')
print('There are %i train images'%count_data_items(TRAINING_FILENAMES))
