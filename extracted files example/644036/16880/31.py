metadata = pd.read_json('../input/deepfake-detection-challenge/train_sample_videos/metadata.json').T

def predict_model(video_fn, model,
                  start_frame=0, end_frame=30,
                  plot_every_x_frames = 5):
    """
    Given a video and model, starting frame and end frame.
    Predict on all frames.
    
    """
    fn = video_fn.split('.')[0]
    label = metadata.loc[video_fn]['label']
    original = metadata.loc[video_fn]['original']
    video_path = f'../input/deepfake-detection-challenge/train_sample_videos/{video_fn}'
    output_path = './'
    test_full_image_network(video_path, model, output_path, start_frame=0, end_frame=30, cuda=False)
    # Read output
    vidcap = cv2.VideoCapture(f'{fn}.avi')
    success,image = vidcap.read()
    count = 0
    fig, axes = plt.subplots(3, 2, figsize=(20, 15))
    axes = axes = axes.flatten()
    i = 0
    while success:
        # Show every xth frame
        if count % plot_every_x_frames == 0:

            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            axes[i].imshow(image)
            axes[i].set_title(f'{fn} - frame {count} - true label: {label}')
            axes[i].xaxis.set_visible(False)
            axes[i].yaxis.set_visible(False)
            i += 1
        success,image = vidcap.read()
        count += 1
    plt.tight_layout()
    plt.show()
