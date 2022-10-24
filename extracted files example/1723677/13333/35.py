from keras.models import load_model
model1 = load_model('Seg_0.h5',custom_objects={'dice_coef':dice_coef,'jaccard_loss':jaccard_loss})
model2 = load_model('Seg_1.h5',custom_objects={'dice_coef':dice_coef,'jaccard_loss':jaccard_loss})
model3 = load_model('Seg_2.h5',custom_objects={'dice_coef':dice_coef,'jaccard_loss':jaccard_loss})
