if TRAIN_MODELS:
    for k in range(1,5):
        print('Computing bb',k,'...',end='')
        train2['b'+str(k)] = train2['e'+str(k)].map(rle2bb)
        print('Computing dice_bb',k,'...',end='')
        train2['s'+str(k)] = train2.apply(lambda x: bb2dice(x['e'+str(k)],x['b'+str(k)]),axis=1)
    print('Done')
    train2.head()
else:
    for k in range(1,5):
        train2['b'+str(k)] = np.load('../input/cloudpred1/bb'+str(k)+'.npy',allow_pickle=True)[:,0]
        train2['s'+str(k)] = np.load('../input/cloudpred1/bb'+str(k)+'.npy',allow_pickle=True)[:,1]
    print('Saving time by loading computed bounding boxes')
