# DISPLAY GENERATED DOGS
plt.figure(figsize=(15,15))
plt.subplots_adjust(hspace=0,wspace=0)
for k in range(100):
    plt.subplot(10,10,k+1)
    img = Image.fromarray( ((output[k,]+1.)/2.*255).astype('uint8') )
    plt.axis('off')
    plt.imshow(img)
plt.show(img)
