def bb2rle(b,shape=(525,350)):
    bb = [0,0,0,0]
    bb[0] = np.min(( np.max((int(b[0]),0)),shape[1] ))
    bb[1] = np.min(( np.max((int(b[1]),0)),shape[0] ))
    bb[2] = np.min(( np.max((int(b[2]),0)),shape[1]-bb[0] ))
    bb[3] = np.min(( np.max((int(b[3]),0)),shape[0]-bb[1] ))
    z = np.ones((bb[3]*2))*bb[2]
    z[::2] = np.arange(bb[3]) * shape[1] + (shape[1]*bb[1]+bb[0]+1)
    z = z.astype(int)
    return ' '.join(str(x) for x in z)

def dice_coef6(y_true_rle, y_pred_prob, y_pred_rle,th):
    if y_pred_prob<th:
        if y_true_rle=='': return 1
        else: return 0
    else:
        y_true_f = rle2mask(y_true_rle,shrink=4)
        y_pred_f = rle2mask(y_pred_rle,shape=(525,350))
        union = np.sum(y_true_f) + np.sum(y_pred_f)
        if union==0: return 1
        intersection = np.sum(y_true_f * y_pred_f)
        return 2. * intersection / union
