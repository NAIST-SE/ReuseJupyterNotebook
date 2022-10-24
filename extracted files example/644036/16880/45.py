torch.nn.Module.dump_patches = True
model_path_23 = '../input/deepfakemodelspackages/faceforensics_models/faceforensics++_models_subset/face_detection/xception/all_c23.p'
model_23 = torch.load(model_path_23, map_location=torch.device('cpu'))
model_path_raw = '../input/deepfakemodelspackages/faceforensics_models/faceforensics++_models_subset/face_detection/xception/all_raw.p'
model_raw = torch.load(model_path_raw, map_location=torch.device('cpu'))
