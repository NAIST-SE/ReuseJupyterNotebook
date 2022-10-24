!pip install tta-wrapper --quiet
from tta_wrapper import tta_segmentation

if DO_TEST:
    model1 = load_model('model_0.h5',custom_objects={'dice_coef':dice_coef,
            'jaccard_loss':jaccard_loss,'AdamAccumulate':AdamAccumulate,
            'kaggle_dice':kaggle_dice,'kaggle_acc':kaggle_acc})
    if USE_TTA:
        model1 = tta_segmentation(model1, h_flip=True, h_shift=(-10, 10), v_flip=True, v_shift=(-10, 10), merge='mean')
    model2 = load_model('model_1.h5',custom_objects={'dice_coef':dice_coef,
            'jaccard_loss':jaccard_loss,'AdamAccumulate':AdamAccumulate,
            'kaggle_dice':kaggle_dice,'kaggle_acc':kaggle_acc})
    if USE_TTA:
        model2 = tta_segmentation(model2, h_flip=True, h_shift=(-10, 10), v_flip=True, v_shift=(-10, 10), merge='mean')
    model3 = load_model('model_2.h5',custom_objects={'dice_coef':dice_coef,
            'jaccard_loss':jaccard_loss,'AdamAccumulate':AdamAccumulate,        
            'kaggle_dice':kaggle_dice,'kaggle_acc':kaggle_acc})
    if USE_TTA:
        model3 = tta_segmentation(model3, h_flip=True, h_shift=(-10, 10), v_flip=True, v_shift=(-10, 10), merge='mean')
