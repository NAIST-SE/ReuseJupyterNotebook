# NEW MODEL FROM OLD TO EXTRACT ACTIVATION MAPS
all_layer_weights = model.layers[-1].get_weights()[0]
cam_model = tf.keras.Model(inputs=model.input, 
        outputs=(model.layers[-4].output, model.layers[-1].output)) 
pr = {0:'NEUTRAL',1:'POSITIVE',2:'NEGATIVE'}
