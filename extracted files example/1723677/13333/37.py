# LOAD CLASSIFICATION PREDICTIONS FROM PREVIOUS KERNEL
# https://www.kaggle.com/cdeotte/cloud-bounding-boxes-cv-0-58
sub['p'] = np.load('../input/cloudpred1/preds.npy').reshape((-1))[:len(sub)]
sub.loc[sub.p<0.5,'EncodedPixels'] = ''

sub.EncodedPixels = sub.EncodedPixels.map(clean)
sub[['Image_Label','EncodedPixels']].to_csv('submission.csv',index=False)
sub.head(25)
