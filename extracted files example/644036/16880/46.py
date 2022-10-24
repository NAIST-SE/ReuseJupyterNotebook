# Read metadata
metadata = pd.read_json('../input/deepfake-detection-challenge/train_sample_videos/metadata.json').T

# Predict Fake
for video_fn in tqdm(metadata.query('label == "FAKE"').sample(77).index):
    video_path = f'../input/deepfake-detection-challenge/train_sample_videos/{video_fn}'
    predictions, outputs, mean_pred, min_pred, max_pred = video_file_frame_pred(video_path, model_23, n_frames=4, cuda=False)
    metadata.loc[video_fn, 'avg_pred_c23'] = mean_pred
    metadata.loc[video_fn, 'min_pred_c23'] = min_pred
    metadata.loc[video_fn, 'max_pred_c23'] = max_pred
    predictions, outputs, mean_pred, min_pred, max_pred = video_file_frame_pred(video_path, model_raw, n_frames=4, cuda=False)
    metadata.loc[video_fn, 'avg_pred_raw'] = mean_pred
    metadata.loc[video_fn, 'min_pred_raw'] = min_pred
    metadata.loc[video_fn, 'max_pred_raw'] = max_pred
    
# Predict Real
for video_fn in tqdm(metadata.query('label == "REAL"').sample(77).index):
    video_path = f'../input/deepfake-detection-challenge/train_sample_videos/{video_fn}'
    predictions, outputs, mean_pred, min_pred, max_pred = video_file_frame_pred(video_path, model_23, n_frames=4, cuda=False)
    metadata.loc[video_fn, 'avg_pred_c23'] = mean_pred
    metadata.loc[video_fn, 'min_pred_c23'] = min_pred
    metadata.loc[video_fn, 'max_pred_c23'] = max_pred
    predictions, outputs, mean_pred, min_pred, max_pred = video_file_frame_pred(video_path, model_raw, n_frames=4, cuda=False)
    metadata.loc[video_fn, 'avg_pred_raw'] = mean_pred
    metadata.loc[video_fn, 'min_pred_raw'] = min_pred
    metadata.loc[video_fn, 'max_pred_raw'] = max_pred
