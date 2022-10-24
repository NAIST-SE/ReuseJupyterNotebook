ids = train['ImageId'].values
fig, axes = plt.subplots(4, 3, figsize=(18, 20))
for i in range(4):
    img = load_img('../input/pku-autonomous-driving/train_images/' + ids[i] + '.jpg')
    img_mask = load_img('../input/pku-autonomous-driving/train_masks/' + ids[i] + '.jpg')
    #plt.subplot(1,2*(1+len(ids)),q*2-1)
    ax=axes[i][0].imshow(img)
    #plt.subplot(1,2*(1+len(ids)),q*2)
    ax=axes[i][1].imshow(img_mask)
    ax=axes[i][2].imshow(img)
    ax=axes[i][2].imshow(img_mask, cmap=plt.cm.viridis, interpolation='none', alpha=0.4)
plt.show()
