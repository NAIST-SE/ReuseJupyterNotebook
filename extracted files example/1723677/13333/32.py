def dice_coef6(y_true_rle, y_pred_prob, y_pred_rle, th):
    if y_pred_prob<th:
        if y_true_rle=='': return 1
        else: return 0
    else:
        y_true_f = rle2maskX(y_true_rle,shrink=4)
        y_pred_f = rle2maskX(y_pred_rle,shape=(525,350))
        union = np.sum(y_true_f) + np.sum(y_pred_f)
        if union==0: return 1
        intersection = np.sum(y_true_f * y_pred_f)
        return 2. * intersection / union
