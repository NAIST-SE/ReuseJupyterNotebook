fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(1, 5, figsize=(20, 10))
img1 = mpimg.imread('../input/lanl-earthquake-spectrogram-images/train_images_no_overlap/train_images_v3/train_0.png')
img2 = mpimg.imread('../input/lanl-earthquake-spectrogram-images/train_images_no_overlap/train_images_v3/train_100.png')
img3 = mpimg.imread('../input/lanl-earthquake-spectrogram-images/train_images_no_overlap/train_images_v3/train_200.png')
img4 = mpimg.imread('../input/lanl-earthquake-spectrogram-images/train_images_no_overlap/train_images_v3/train_300.png')
img5 = mpimg.imread('../input/lanl-earthquake-spectrogram-images/train_images_no_overlap/train_images_v3/train_400.png')
ax1.imshow(img1)
ax1.set_title('TTF - {:0.4f}'.format(train_labels.loc[train_labels['seg_id'] == 'train_0']['target'].values[0]), fontsize=25)
ax2.imshow(img2)
ax2.set_title('TTF - {:0.4f}'.format(train_labels.loc[train_labels['seg_id'] == 'train_100']['target'].values[0]), fontsize=25)
ax3.imshow(img3)
ax3.set_title('TTF - {:0.4f}'.format(train_labels.loc[train_labels['seg_id'] == 'train_200']['target'].values[0]), fontsize=25)
ax4.imshow(img4)
ax4.set_title('TTF - {:0.4f}'.format(train_labels.loc[train_labels['seg_id'] == 'train_300']['target'].values[0]), fontsize=25)
ax5.imshow(img5)
ax5.set_title('TTF - {:0.4f}'.format(train_labels.loc[train_labels['seg_id'] == 'train_400']['target'].values[0]), fontsize=25)
ax1.axis('off')
ax2.axis('off')
ax3.axis('off')
ax4.axis('off')
ax5.axis('off')
plt.tight_layout()
plt.show()
