# DISPLAY LATENT WALK
plt.figure(figsize=(int(2*COLS),int(2*ROWS)))
plt.subplots_adjust(hspace=0,wspace=0)
for k in range(ROWS*COLS):
    plt.subplot(ROWS,COLS,k+1)
    img = Image.fromarray( ((output[k,]+1.)/2.*255).astype('uint8') )
    plt.axis('off')
    plt.imshow(img)
plt.show(img)
