model_path_face_allraw = '../input/deepfakemodelspackages/faceforensics_models/faceforensics++_models_subset/face_detection/xception/all_raw.p'
model_face_allraw = torch.load(model_path_face_allraw, map_location=torch.device('cpu'))
