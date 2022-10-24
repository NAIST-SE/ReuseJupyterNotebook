bs = 10
train_labels['path'] = '../input/lanl-earthquake-spectrogram-images/train_images_no_overlap/train_images_v3/' + train_labels['seg_id'] + '.png'
#valid_idx = train_labels[:10000].loc[train_labels['quake_number'].isin([1, 5, 8])].index
#train_idx = train_labels[:10000].loc[~train_labels['quake_number'].isin([1, 5, 8])].index
data = (ImageList.from_df(train_labels[:-1], path='./', cols='path')
        #.split_by_idxs(train_idx=train_idx, valid_idx=valid_idx)
        .split_by_rand_pct(0.1)
        .label_from_df('target', label_cls=FloatList)
        #.transform(get_transforms(), size=255)
        .databunch(bs=bs))
