model_path_full23 = '../input/deepfakemodelspackages/faceforensics_models/faceforensics++_models_subset/full/xception/full_c23.p'
model_full_c23 = torch.load(model_path_full23, map_location=torch.device('cpu'))
