sub = pd.read_csv('../input/understanding_cloud_organization/sample_submission.csv')
sub['Image'] = sub['Image_Label'].map(lambda x: x.split('.')[0])
sub['Label'] = sub['Image_Label'].map(lambda x: x.split('_')[1])
# LOAD TEST CLASSIFIER PREDICTIONS
sub['p'] = pd.read_csv('../input/cloud-classifiers/pred_cls.csv').p.values
sub['p'] += np.load('../input/cloud-classifiers/pred_cls0.npy').reshape((-1)) * 0.5
sub['p'] += pd.read_csv('../input/cloud-classifiers/pred_cls3.csv').p.values * 3.0
sub['p'] += np.load('/kaggle/input/cloud-classifiers/pred_cls4b.npy') * 0.6
sub['p'] /= 5.1

train = pd.read_csv('../input/cloud-images-resized/train_384x576.csv')
train['Image'] = train['Image_Label'].map(lambda x: x.split('.')[0])
train['Label'] = train['Image_Label'].map(lambda x: x.split('_')[1])
train2 = pd.DataFrame({'Image':train['Image'][::4]})
train2['e1'] = train['EncodedPixels'][::4].values
train2['e2'] = train['EncodedPixels'][1::4].values
train2['e3'] = train['EncodedPixels'][2::4].values
train2['e4'] = train['EncodedPixels'][3::4].values
train2.set_index('Image',inplace=True,drop=True)
train2.fillna('',inplace=True); train2.head()
train2[['d1','d2','d3','d4']] = (train2[['e1','e2','e3','e4']]!='').astype('int8')
for k in range(1,5): train2['o'+str(k)] = 0
# LOAD TRAIN CLASSIFIER PREDICTIONS
train2[['o1','o2','o3','o4']] = np.load('../input/cloud-classifiers/oof_cls.npy')
train2[['o1','o2','o3','o4']] += np.load('../input/cloud-classifiers/oof_cls0.npy') * 0.5
train2[['o1','o2','o3','o4']] += np.load('../input/cloud-classifiers/oof_cls3.npy') * 3.0
train2[['o1','o2','o3','o4']] += np.load('../input/cloud-classifiers/oof_cls4b.npy') * 0.6
train2[['o1','o2','o3','o4']] /= 5.1
train2.head()
