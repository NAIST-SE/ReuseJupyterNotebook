model_path = '../input/deepfakemodelspackages/faceforensics_models/faceforensics++_models_subset/full/xception/full_raw.p'
model = torch.load(model_path, map_location=torch.device('cpu'))
