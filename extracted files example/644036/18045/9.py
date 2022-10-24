for db in drift_batches:
    d = tt.query('sbatch == @db')
    def shift_and_anchor_count(shift):
        anchor_count = 0
        shifted_signal = (d['signal'] + shift).round(4)
        for a in anchors:
    #         print(a)
            n_anchors = (shifted_signal == a).sum()
    #         print(n_anchors)
            anchor_count += n_anchors
    #     print(f'Shift {shift} ---> anchor count: {anchor_count}')
    

        return -anchor_count
    res = minimize(shift_and_anchor_count, [0], method='Powell', tol=1e-6)
    opt_shift = res['x']
    print(f'Drift batch {db} - optimal shift {opt_shift}')
    tt.loc[tt['sbatch'] == db, 'signal_shift'] = (tt.loc[tt['sbatch'] == db]['signal'] - opt_shift).round(4)
