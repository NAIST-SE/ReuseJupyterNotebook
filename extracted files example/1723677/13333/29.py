! pip install segmentation-models

from segmentation_models import Unet,FPN
from segmentation_models.losses import bce_jaccard_loss, jaccard_loss
from keras.optimizers import Adam

def build_model():
    #model = Unet('resnet34', input_shape=(None,None,3), classes=4, activation='sigmoid')
    model = FPN('efficientnetb2', input_shape=(None, None, 3), classes=4, activation='sigmoid')
    #model = FPN('inceptionv3', input_shape=(None, None, 3), classes=4, activation='sigmoid')

    #model.compile(optimizer=Adam(lr=0.001), loss='binary_crossentropy', metrics=[dice_coef])
    #model.compile(optimizer=Adam(lr=0.0001), loss=bce_jaccard_loss, metrics=[dice_coef])
    model.compile(optimizer=Adam(lr=0.0001), loss=jaccard_loss, metrics=[dice_coef])
    #model.compile(optimizer=Adam(lr=0.0001), loss=dice_coef_loss, metrics=[dice_coef])
    return model
