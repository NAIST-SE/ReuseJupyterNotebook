fig, ax = plt.subplots(figsize=(15, 15))
plt.imshow(img)
plt.imshow(mask, cmap=plt.cm.viridis, interpolation='none', alpha=0.5)
plt.show()
