DISPLAY_EVERY = 10

def display_images(model, test_input, labs):
    predictions = model([test_input,labs], training=False)
    fig = plt.figure(figsize=(16,4))
    for i in range(predictions.shape[0]):
        plt.subplot(2, 8, i+1)
        plt.imshow( (predictions[i, :, :, :]+1.)/2. )
        plt.axis('off')
    plt.show()
    
def generate_latent_points(latent_dim, n_samples):
    return tf.random.truncated_normal((n_samples,latent_dim))

def train(dataset, epochs):
    all_gl = np.array([]); all_dl = np.array([])
    
    for epoch in range(epochs):
        start = time.time()
        gl = []; dl = []
           
        # TENSOR FLOW DATA.DATASET HAS A BUG AND WONT SHUFFLE ON ITS OWN :-(
        # https://github.com/tensorflow/tensorflow/issues/27680
        idx = np.arange(idxIn)
        np.random.shuffle(idx)
        dataset = (tf.data.Dataset.from_tensor_slices((imagesIn[idx,:,:,:],namesIn[idx]))
            .map(flip).map(crop).batch(BATCH_SIZE,drop_remainder=True))
        
        # TRAIN ACGAN
        for i,image_batch in enumerate(dataset):
            gg,dd = train_step(image_batch,generator,discriminator,
                        generator_optimizer, discriminator_optimizer)
            gl.append(gg); dl.append(dd)
        all_gl = np.append(all_gl,np.array([gl]))
        all_dl = np.append(all_dl,np.array([dl]))
        
        # EXPONENTIALLY DECAY LEARNING RATES
        if epoch>180: learning_rate.assign(learning_rate*0.95)
        
        # DISPLAY PROGRESS
        if epoch%DISPLAY_EVERY==0:
            # PLOT EPOCH LOSS
            plt.figure(figsize=(16,2))
            plt.plot(np.arange(len(gl)),gl,label='Gen_loss')
            plt.plot(np.arange(len(dl)),dl,label='Disc_loss')
            plt.legend()
            plt.title('Epoch '+str(epoch)+' Loss')
            ymax = plt.ylim()[1]
            plt.show()
            
            # PLOT ALL TIME LOSS
            plt.figure(figsize=(16,2))
            plt.plot(np.arange(len(all_gl)),all_gl,label='Gen_loss')
            plt.plot(np.arange(len(all_dl)),all_dl,label='Disc_loss')
            plt.legend()
            plt.ylim((0,np.min([1.1*np.max(all_gl),2*ymax])))
            plt.title('All Time Loss')
            plt.show()

            # DISPLAY IMAGES FROM TRAIN PROGRESS
            seed = generate_latent_points(noise_dim, num_examples)
            labs = tf.cast(120*tf.random.uniform((num_examples,1)),tf.int8)
            display_images(generator, seed, labs)
            
            # PRINT STATS
            print('EPOCH',epoch,'took',np.round(time.time()-start,1),'sec')
            print('Gen_loss mean=',np.mean(gl),'std=',np.std(gl))
            print('Disc_loss mean=',np.mean(dl),'std=',np.std(dl))
            print('Learning rate = ',end='')
            tf.print(discriminator_optimizer._lr)
            
        x = gc.collect()
        tt = np.round( (time.time() - kernel_start)/60,1 )
        if tt > LIMIT*60: break
