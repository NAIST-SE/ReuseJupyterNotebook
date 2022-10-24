for db in drift_batches:
    d = tt.query('sbatch == @db')
    def shift_and_anchor_count(shift):
        shift = shift/1000
        anchor_count = 0
        shifted_signal = (d['signal'] + shift).round(4)
        for a in anchors:
            n_anchors = (shifted_signal == a).sum()
            anchor_count += n_anchors
            # Penalize for high counts neighbors numbers being high
            pprior = round(a - 0.0002, 4)
            prior = round(a - 0.0001, 4)
            post = round(a + 0.0001, 4)
            ppost = round(a + 0.0002, 4)
            n_anchor_prior = (shifted_signal == prior).sum()
            n_anchor_pprior = (shifted_signal == pprior).sum()
#             print(n_anchor_prior)
            anchor_count -= (prior - pprior)
            n_anchor_post = (shifted_signal == post).sum()
            n_anchor_ppost = (shifted_signal == ppost).sum()
            anchor_count -= (post - ppost)
#         print()
        return -anchor_count
    res = minimize(shift_and_anchor_count, [0], method='Powell') #, bounds=(-0.0001, 0.0001))
    opt_shift = res['x']
    print(f'Drift batch {db} - optimal shift {opt_shift}')
    tt.loc[tt['sbatch'] == db, 'signal_shift'] = (tt.loc[tt['sbatch'] == db]['signal'] + (opt_shift/1000)).round(4)
