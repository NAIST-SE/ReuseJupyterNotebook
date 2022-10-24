plt.rcParams["axes.grid"] = False

train_ids = train['ImageId'].values
img_name = train.loc[2742]['ImageId']
fig, ax = plt.subplots(figsize=(15, 15))
img = load_img('../input/pku-autonomous-driving/train_images/' + img_name + '.jpg')
plt.imshow(img)
plt.show()
