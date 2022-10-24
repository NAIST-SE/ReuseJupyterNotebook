model_path_face_all_c40 = '../input/deepfakemodelspackages/faceforensics_models/faceforensics++_models_subset/face_detection/xception/all_c40.p'
model_face_all_c40 = torch.load(model_path_face_all_c40, map_location=torch.device('cpu'))
