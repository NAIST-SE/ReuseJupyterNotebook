for j in range(4):
    rles = []
    print('Converting bb2rle',j,'..., ',end='')
    for k in range( oof_bb.shape[0] ):
        rle = bb2rle( (oof_bb[k,0,j],oof_bb[k,1,j],oof_bb[k,2,j],oof_bb[k,3,j]) )
        rles.append(rle)
    train2['bb'+str(j+1)] = rles
print('Done')
