mse = tf.keras.losses.MeanSquaredError()

print('Display Random Dogs by Breed')
print()
for j in np.random.randint(0,120,25):
    # GENERATE DOGS
    seed = generate_latent_points(noise_dim, 10)
    labs = tf.cast( j*np.ones((10,1)), tf.int8)
    predictions = generator([seed,labs], training=False); d = 0   
    # GET BREED NAME    
    br = np.argwhere( namesIn==j ).flatten()
    bd = le.inverse_transform(np.array([j]))[0].capitalize()
    # CALCULATE VARIETY
    for k in range(4): d += mse(predictions[k,:,:,:],predictions[k+1,:,:,:]) 
    d = np.round( np.array(d),1 )
    if d<1.0: 
        print(bd,'had mode collapse. No display. (variety =',d,')')
        continue
    # DISPLAY DOGS
    print(bd,'REAL DOGS on top. FAKE DOGS on bottom. (variety =',d,')')
    plt.figure(figsize=(15,9))
    for i in range(5):
        plt.subplot(3,5,i+1)
        plt.imshow( (imagesIn[br[i],:,:,:]+1.)/2. )
        plt.axis('off')
    for i in range(10):
        plt.subplot(3,5,i+6)
        plt.imshow( (predictions[i,:,:,:]+1.)/2. )
        plt.axis('off')
    plt.show()
