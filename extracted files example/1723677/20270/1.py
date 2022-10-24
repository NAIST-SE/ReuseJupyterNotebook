# PATHS TO IMAGES
PATH = '../input/melanoma-merged-external-data-512x512-jpeg/512x512-dataset-melanoma/512x512-dataset-melanoma/'
PATH2 = '../input/melanoma-merged-external-data-512x512-jpeg/512x512-test/512x512-test/'
IMGS = os.listdir(PATH); IMGS2 = os.listdir(PATH2)
print('There are %i train images and %i test images'%(len(IMGS),len(IMGS2)))
