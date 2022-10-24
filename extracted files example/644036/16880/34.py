model_path_full_c40 = '../input/deepfakemodelspackages/faceforensics_models/faceforensics++_models_subset/full/xception/full_c40.p'
model_full_c40 = torch.load(model_path_full_c40, map_location=torch.device('cpu'))
