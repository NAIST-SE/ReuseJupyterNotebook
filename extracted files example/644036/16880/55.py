for video_fn in tqdm(ss['filename'].unique()):
    video_path = f'../input/deepfake-detection-challenge/test_videos/{video_fn}'
    predictions, outputs, mean_pred, min_pred, max_pred = video_file_frame_pred(video_path, model, n_frames=4, cuda=False)
    ss.loc[ss['filename'] == video_fn, 'avg_pred'] = mean_pred
    ss.loc[ss['filename'] == video_fn, 'min_pred'] = min_pred
    ss.loc[ss['filename'] == video_fn, 'max_pred'] = max_pred
