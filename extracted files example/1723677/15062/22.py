# COMPUTE LB SCORE
mm = []; ss =[]; ff = []
user_images_unzipped_path = '../tmp/images/'
images_path = [user_images_unzipped_path,'../input/generative-dog-images/all-dogs/all-dogs/']
public_path = '../input/dog-face-generation-competition-kid-metric-input/classify_image_graph_def.pb'

fid_epsilon = 10e-15

fid_value_public, distance_public, mm, ss, ff = calculate_kid_given_paths(images_path, 'Inception', public_path, mm=mm, ss=ss, ff=ff)
distance_public = distance_thresholding(distance_public, model_params['Inception']['cosine_distance_eps'])
print("FID_public: ", fid_value_public, "distance_public: ", distance_public, "multiplied_public: ",
          fid_value_public /(distance_public + fid_epsilon))
