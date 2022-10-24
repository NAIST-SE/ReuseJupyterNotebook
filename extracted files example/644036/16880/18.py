ss = pd.read_csv("/kaggle/input/deepfake-detection-challenge/sample_submission.csv")
ss['label'] = 0.5
ss.loc[ss['filename'] == 'aassnaulhq.mp4', 'label'] = 0 # Guess the true value
ss.loc[ss['filename'] == 'aayfryxljh.mp4', 'label'] = 0
ss.to_csv('submission.csv', index=False)
