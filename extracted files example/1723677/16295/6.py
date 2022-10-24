model = build_model()
    
sv = tf.keras.callbacks.ModelCheckpoint(
        'cam.h5', monitor='val_loss', verbose=1, save_best_only=True,
        save_weights_only=True, mode='auto', save_freq='epoch')
    
model.fit([ids[idxT,],att[idxT,],tok[idxT,]], tar4[idxT], 
          validation_data = ([ids[idxV,],att[idxV,],tok[idxV,]], tar4[idxV]),
          epochs=2, batch_size=32, verbose=1, callbacks=[sv])

model.load_weights('cam.h5')
