EPOCHS = 250
num_examples = 16

@ tf.function
def train_step(images,generator,discriminator,generator_optimizer,discriminator_optimizer):
        
    bce = tf.keras.losses.BinaryCrossentropy(from_logits=True,label_smoothing=0.4)
    bce2 = tf.keras.losses.BinaryCrossentropy(from_logits=False,label_smoothing=0.4)
    noise = tf.random.normal((32,128)) # update noise_dim here
    labs = tf.cast(120*tf.random.uniform((32,)),tf.int32)
    
    # USE GRADIENT TAPE TO CALCULATE GRADIENTS
    with tf.GradientTape() as gen_tape, tf.GradientTape() as disc_tape:       
        generated_images = generator([noise,labs], training=True)
        real_cat, real_output = discriminator([images[0],images[1]], training=True)
        fake_cat, fake_output = discriminator([generated_images,labs], training=True)
    
        # GENERATOR LOSS 
        gen_loss = (tf.reduce_mean( (real_output - tf.reduce_mean(fake_output,0) + tf.ones_like(real_output))**2,0 )
        + tf.reduce_mean( (fake_output - tf.reduce_mean(real_output,0) - tf.ones_like(real_output))**2,0 ) )/2.
        
        # DISCRIMINATOR LOSS
        disc_loss = bce(tf.ones_like(real_output), real_output) + bce(tf.zeros_like(fake_output), fake_output)           
        real_cat2 = tf.one_hot(tf.cast(images[1],tf.int32),121,dtype=tf.int32)
        fake_cat2 = tf.one_hot(120*tf.ones((32,),tf.int32),121,dtype=tf.int32)
        disc_loss += bce2(real_cat2,real_cat) + bce2(fake_cat2,fake_cat) 
        
    # BACK PROPAGATE ERROR
    gradients_of_generator = gen_tape.gradient(gen_loss, generator.trainable_variables)
    gradients_of_discriminator = disc_tape.gradient(disc_loss, discriminator.trainable_variables)
    generator_optimizer.apply_gradients(zip(gradients_of_generator, generator.trainable_variables))
    discriminator_optimizer.apply_gradients(zip(gradients_of_discriminator, discriminator.trainable_variables))
       
    return gen_loss, disc_loss

print('Training started. Displaying every '+str(DISPLAY_EVERY)+'th epoch.')
train(ds, EPOCHS)
