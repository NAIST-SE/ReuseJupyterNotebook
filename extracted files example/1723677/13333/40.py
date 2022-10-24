def mask2rleXXX(img0, shape=(576,384), grow=(525,350)):
    '''
    img: numpy array, 1 - mask, 0 - background
    Returns run length as string formated
    '''
    a = (shape[1]-img0.shape[0])//2
    b = (shape[0]-img0.shape[1])//2
    img = np.zeros((shape[1],shape[0]),dtype=np.uint8)
    img[a:a+img0.shape[0],b:b+img0.shape[1]] = img0
    img = cv2.resize(img,grow)
    
    pixels= img.T.flatten()
    pixels = np.concatenate([[0], pixels, [0]])
    runs = np.where(pixels[1:] != pixels[:-1])[0] + 1
    runs[1::2] -= runs[::2]
    return ' '.join(str(x) for x in runs)

def rle2maskX(mask_rle, shape=(2100,1400), shrink=1):
    s = mask_rle.split()
    starts, lengths = [np.asarray(x, dtype=int) for x in (s[0:][::2], s[1:][::2])]
    starts -= 1
    ends = starts + lengths
    img = np.zeros(shape[0]*shape[1], dtype=np.uint8)
    for lo, hi in zip(starts, ends):
        img[lo:hi] = 1
    return img.reshape(shape).T[::shrink,::shrink]

def dice_coef(y_true, y_pred, smooth=1):
    y_true_f = K.flatten(y_true)
    y_pred_f = K.flatten(y_pred)
    intersection = K.sum(y_true_f * y_pred_f)
    return (2. * intersection + smooth) / (K.sum(y_true_f) + K.sum(y_pred_f) + smooth)
