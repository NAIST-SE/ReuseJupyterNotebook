fig, ax = plt.subplots(figsize=(15, 15))
mask = load_img('../input/pku-autonomous-driving/train_masks/' + img_name + '.jpg')
plt.imshow(mask)
plt.show()
