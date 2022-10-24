# SUBMIT 84 IMAGES OF EACH OF 119 BREEDS and 4 of breed 120
z = zipfile.PyZipFile('images.zip', mode='w')
for i in range(120):
    ct = 84
    if i==119: ct=4
    seed = generate_latent_points(noise_dim, ct)
    labs = tf.cast( i*np.ones((ct,1)), tf.int8)
    predictions = generator([seed,labs], training=False)
    predictions = 255*((np.array(predictions)+1.)/2.)
    for j in range(ct):
        img = Image.fromarray( predictions[j,:,:,:].astype('uint8') )
        f = str(i*84+j)+'.png'
        img.save(f,'PNG'); z.write(f); os.remove(f)
    #if (i%10==0)|(i==119): print(i*84)
z.close()
