def onehot(image,label):
    CLASSES = 104
    return image,tf.one_hot(label,CLASSES)
