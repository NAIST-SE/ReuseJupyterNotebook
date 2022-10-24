sub = pd.read_csv('../input/liverpool-ion-switching/sample_submission.csv')
sub.open_channels = np.median( np.stack([p1,p2,p3]).T, axis=1 ).astype('int8')
sub.to_csv('submission.csv', index=False, float_format='%.4f')
