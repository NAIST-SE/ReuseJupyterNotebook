# GENERATE SAMPLES
# TRUNCATION VARIABLE AFFECTS QUALITY AND DIVERSITY
truncation=1.0
for k in range(100):
    SAMPLES = 100
    class_vector = np.zeros((SAMPLES,1000),dtype=np.float32)
    for x in range(SAMPLES): 
        class_vector[x,np.random.randint(151,281)]=1 #(281,294) are cats
    # CATEGORY LIST HERE: https://gist.github.com/yrevar/942d3a0ac09ec9e5eb3a
    noise_vector = truncated_noise_sample(truncation=truncation, batch_size=SAMPLES)

    # All in tensors
    noise_vector = torch.from_numpy(noise_vector)
    class_vector = torch.from_numpy(class_vector)

    # If you have a GPU, put everything on cuda
    noise_vector = noise_vector.to('cuda')
    class_vector = class_vector.to('cuda')
    model.to('cuda')

    # Generate an image
    with torch.no_grad():
        output = model(noise_vector, class_vector, truncation)

    # If you have a GPU put back on CPU
    output = output.to('cpu')
    output = output.numpy().transpose(0, 2, 3, 1)
    
    for j in range(100):
        img = Image.fromarray( ((output[j,]+1.)/2.*255).astype('uint8') )
        img = img.resize((64,64), Image.ANTIALIAS)
        img.save('../tmp/images/'+str(k*100+j)+'.png','PNG')
    #if k%10==0: print(k)
