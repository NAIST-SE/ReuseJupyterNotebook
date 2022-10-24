def rle2mask(mask_rle, shape=(2100,1400), shrink=1):
    s = mask_rle.split()
    starts, lengths = [np.asarray(x, dtype=int) for x in (s[0:][::2], s[1:][::2])]
    starts -= 1
    ends = starts + lengths
    img = np.zeros(shape[0]*shape[1], dtype=np.uint8)
    for lo, hi in zip(starts, ends):
        img[lo:hi] = 1
    return img.reshape(shape).T[::shrink,::shrink]

def rle2bb(rle):
    if rle=='': return (0,0,0,0)
    mask = rle2mask(rle)
    z = np.argwhere(mask==1)
    mn_x = np.min( z[:,0] )
    mx_x = np.max( z[:,0] )
    mn_y = np.min( z[:,1] )
    mx_y = np.max( z[:,1] )
    return (mn_x,mn_y,mx_x-mn_x,mx_y-mn_y)

def bb2dice(rle,bb,shape=(2100,1400)):
    mask1 = rle2mask(rle,shape)
    mask2 = np.zeros((shape[1],shape[0]))
    mask2[bb[0]:bb[0]+bb[2],bb[1]:bb[1]+bb[3]]=1
    union = np.sum(mask1) + np.sum(mask2)
    if union==0: return 1
    intersection = np.sum(mask1*mask2)
    return 2.*intersection/union
