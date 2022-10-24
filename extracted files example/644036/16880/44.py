def video_file_frame_pred(video_path, model,
                          start_frame=0, end_frame=300,
                          cuda=True, n_frames=5):
    """
    Predict and give result as numpy array
    """
    pred_frames = [int(round(x)) for x in np.linspace(start_frame, end_frame, n_frames)]
    predictions = []
    outputs = []
    # print('Starting: {}'.format(video_path))

    # Read and write
    reader = cv2.VideoCapture(video_path)

    video_fn = video_path.split('/')[-1].split('.')[0]+'.avi'
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    fps = reader.get(cv2.CAP_PROP_FPS)
    num_frames = int(reader.get(cv2.CAP_PROP_FRAME_COUNT))
    writer = None

    # Face detector
    face_detector = dlib.get_frontal_face_detector()

    # Text variables
    font_face = cv2.FONT_HERSHEY_SIMPLEX
    thickness = 2
    font_scale = 1

    # Frame numbers and length of output video
    frame_num = 0
    assert start_frame < num_frames - 1
    end_frame = end_frame if end_frame else num_frames
    while reader.isOpened():
        _, image = reader.read()
        if image is None:
            break
        frame_num += 1
        if frame_num in pred_frames:
            height, width = image.shape[:2]
            # 2. Detect with dlib
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            faces = face_detector(gray, 1)
            if len(faces):
                # For now only take biggest face
                face = faces[0]
                # --- Prediction ---------------------------------------------------
                # Face crop with dlib and bounding box scale enlargement
                x, y, size = get_boundingbox(face, width, height)
                cropped_face = image[y:y+size, x:x+size]

                # Actual prediction using our model
                prediction, output = predict_with_model(cropped_face, model,
                                                        cuda=cuda)
                predictions.append(prediction)
                outputs.append(output)
                # ------------------------------------------------------------------
        if frame_num >= end_frame:
            break
    # Figure out how to do this with torch
    preds_np = [x.detach().cpu().numpy()[0][1] for x in outputs]
    if len(preds_np) == 0:
        return predictions, outputs, 0.5, 0.5, 0.5
    try:
        mean_pred = np.mean(preds_np)
    except:
        # couldnt find faces
        mean_pred = 0.5
    min_pred = np.min(preds_np)
    max_pred = np.max(preds_np)
    return predictions, outputs, mean_pred, min_pred, max_pred
