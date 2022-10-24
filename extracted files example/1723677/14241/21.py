# SAVE MODEL
model.save('UNET.h5')

# LOAD MODEL
from keras.models import load_model
model = load_model('UNET.h5',custom_objects={'dice_coef':dice_coef})

# PREDICT 1 BATCH TEST DATASET
test = pd.read_csv(path + 'sample_submission.csv')
test['ImageId'] = test['ImageId_ClassId'].map(lambda x: x.split('_')[0])
test_batches = DataGenerator(test.iloc[::4],subset='test',batch_size=256,preprocess=preprocess)
test_preds = model.predict_generator(test_batches,steps=1,verbose=1)

# NEXT CONVERT MASKS TO RLE, ADD TO CSV, PROCESS REMAINING BATCHES, AND SUBMIT !!
