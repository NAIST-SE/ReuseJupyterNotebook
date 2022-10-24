def kaggle_acc(y_true, y_pred0, pix=0.5, area=24000, dim=(352,544)):
 
    # PIXEL THRESHOLD
    y_pred = K.cast( K.greater(y_pred0,pix), K.floatx() )
    
    # MIN AREA THRESHOLD
    s = K.sum(y_pred, axis=(1,2))
    s = K.cast( K.greater(s, area), K.floatx() )

    # REMOVE MIN AREA
    s = K.reshape(s,(-1,1))
    s = K.repeat(s,dim[0]*dim[1])
    s = K.reshape(s,(-1,1))
    y_pred = K.permute_dimensions(y_pred,(0,3,1,2))
    y_pred = K.reshape(y_pred,shape=(-1,1))
    y_pred = s*y_pred
    y_pred = K.reshape(y_pred,(-1,y_pred0.shape[3],dim[0],dim[1]))
    y_pred = K.permute_dimensions(y_pred,(0,2,3,1))

    # COMPUTE KAGGLE ACC
    total_y_true = K.sum(y_true, axis=(1,2))
    total_y_true = K.cast( K.greater(total_y_true, 0), K.floatx() )

    total_y_pred = K.sum(y_pred, axis=(1,2))
    total_y_pred = K.cast( K.greater(total_y_pred, 0), K.floatx() )

    return 1 - K.mean( K.abs( total_y_pred - total_y_true ) )


def kaggle_dice(y_true, y_pred0, pix=0.5, area=24000, dim=(352,544)):
 
    # PIXEL THRESHOLD
    y_pred = K.cast( K.greater(y_pred0,pix), K.floatx() )
    
    # MIN AREA THRESHOLD
    s = K.sum(y_pred, axis=(1,2))
    s = K.cast( K.greater(s, area), K.floatx() )

    # REMOVE MIN AREA
    s = K.reshape(s,(-1,1))
    s = K.repeat(s,dim[0]*dim[1])
    s = K.reshape(s,(-1,1))
    y_pred = K.permute_dimensions(y_pred,(0,3,1,2))
    y_pred = K.reshape(y_pred,shape=(-1,1))
    y_pred = s*y_pred
    y_pred = K.reshape(y_pred,(-1,y_pred0.shape[3],dim[0],dim[1]))
    y_pred = K.permute_dimensions(y_pred,(0,2,3,1))

    # COMPUTE KAGGLE DICE
    intersection = K.sum(y_true * y_pred, axis=(1,2))
    total_y_true = K.sum(y_true, axis=(1,2))
    total_y_pred = K.sum(y_pred, axis=(1,2))
    return K.mean( (2*intersection+1e-9) / (total_y_true+total_y_pred+1e-9) )
