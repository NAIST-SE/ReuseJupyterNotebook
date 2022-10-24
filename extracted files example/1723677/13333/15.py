sub['pr'] = preds.reshape((-1))
sub['EncodedPixels'] = ''
for j in range(4):
    rles = []
    print('Converting bb2rle',j,'..., ',end='')
    for k in range( preds_bb.shape[0] ):
        rle = bb2rle( (preds_bb[k,0,j],preds_bb[k,1,j],preds_bb[k,2,j],preds_bb[k,3,j]) )
        rles.append(rle)
    sub.iloc[j::4,1] = rles
print('Done')
sub.loc[sub.pr<0.65,'EncodedPixels'] = ''
sub[['Image_Label','EncodedPixels']].to_csv('submission.csv',index=False)
sub.head(25)
