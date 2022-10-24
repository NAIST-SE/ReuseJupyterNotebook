def mask2rleX(img0, shape=(1050,700), shrink=2):
    # USAGE: embeds into size shape, then shrinks, then outputs rle
    # EXAMPLE: img0 can be 600x1000. It will center load into
    # a mask of 700x1050 then the mask is downsampled to 350x525
    # finally the rle is outputted. 
    a = (shape[1]-img0.shape[0])//2
    b = (shape[0]-img0.shape[1])//2
    img = np.zeros((shape[1],shape[0]))
    img[a:a+img0.shape[0],b:b+img0.shape[1]] = img0
    img = img[::shrink,::shrink]
    
    pixels= img.T.flatten()
    pixels = np.concatenate([[0], pixels, [0]])
    runs = np.where(pixels[1:] != pixels[:-1])[0] + 1
    runs[1::2] -= runs[::2]
    return ' '.join(str(x) for x in runs)

def rle2maskX(mask_rle, shape=(2100,1400), shrink=1):
    # Converts rle to mask size shape then downsamples by shrink
    s = mask_rle.split()
    starts, lengths = [np.asarray(x, dtype=int) for x in (s[0:][::2], s[1:][::2])]
    starts -= 1
    ends = starts + lengths
    img = np.zeros(shape[0]*shape[1], dtype=np.uint8)
    for lo, hi in zip(starts, ends):
        img[lo:hi] = 1
    return img.reshape(shape).T[::shrink,::shrink]

def mask2contour(mask, width=5):
    w = mask.shape[1]
    h = mask.shape[0]
    mask2 = np.concatenate([mask[:,width:],np.zeros((h,width))],axis=1)
    mask2 = np.logical_xor(mask,mask2)
    mask3 = np.concatenate([mask[width:,:],np.zeros((width,w))],axis=0)
    mask3 = np.logical_xor(mask,mask3)
    return np.logical_or(mask2,mask3) 

def clean(rle,sz=20000):
    if rle=='': return ''
    mask = rle2maskX(rle,shape=(525,350))
    num_component, component = cv2.connectedComponents(np.uint8(mask))
    mask2 = np.zeros((350,525))
    for i in range(1,num_component):
        y = (component==i)
        if np.sum(y)>=sz: mask2 += y
    return mask2rleX(mask2,shape=(525,350), shrink=1)
