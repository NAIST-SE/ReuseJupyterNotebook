model, *_ = model_selection(modelname='xception', num_out_classes=2)
model_path_face_allc23 = '../input/deepfakemodelspackages/faceforensics_models/faceforensics++_models_subset/face_detection/xception/all_c23.p'
model_face_all_c23 = torch.load(model_path_face_allc23, map_location=torch.device('cpu'))
