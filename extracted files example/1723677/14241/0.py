import os, numpy as np
from PIL import Image 

TRAIN_IMG = os.listdir('../input/severstal-steel-defect-detection/train_images')
TEST_IMG = os.listdir('../input/severstal-steel-defect-detection/test_images')
print('Original train count =',len(TRAIN_IMG),', Original test count =',len(TEST_IMG))
print('New train count = 1801 , New test count = 1801')
os.mkdir('../tmp/')
os.mkdir('../tmp/train_images/')
r = np.random.choice(TRAIN_IMG,len(TEST_IMG),replace=False)
for i,f in enumerate(r):
    img = Image.open('../input/severstal-steel-defect-detection/train_images/'+f)
    img.save('../tmp/train_images/'+f)
os.mkdir('../tmp/test_images/')
for i,f in enumerate(TEST_IMG):
    img = Image.open('../input/severstal-steel-defect-detection/test_images/'+f)
    img.save('../tmp/test_images/'+f)
