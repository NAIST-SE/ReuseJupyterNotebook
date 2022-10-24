preds_df = metadata.dropna(subset=['avg_pred_raw']).copy()
preds_df['label_binary'] = 0
preds_df.loc[preds_df['label'] == "FAKE", 'label_binary'] = 1
preds_df[['min_pred_c23','max_pred_c23',
          'min_pred_raw','max_pred_raw']] = preds_df[['min_pred_c23','max_pred_c23',
                                                      'min_pred_raw','max_pred_raw']].fillna(0.5)
preds_df['naive_pred'] = 0.5
score_avg23 = log_loss(preds_df['label_binary'], preds_df['avg_pred_c23'])
score_min23 = log_loss(preds_df['label_binary'], preds_df['min_pred_c23'])
score_max23 = log_loss(preds_df['label_binary'], preds_df['max_pred_c23'])
score_avgraw = log_loss(preds_df['label_binary'], preds_df['avg_pred_raw'])
score_minraw = log_loss(preds_df['label_binary'], preds_df['min_pred_raw'])
score_maxraw = log_loss(preds_df['label_binary'], preds_df['max_pred_raw'])
score_naive = log_loss(preds_df['label_binary'], preds_df['naive_pred'])
preds_df['max_pred_clipped'] = preds_df['max_pred_c23'].clip(0.4, 1)
score_max_clipped = log_loss(preds_df['label_binary'], preds_df['max_pred_clipped'])
preds_df['max_pred_clipped_raw'] = preds_df['max_pred_raw'].clip(0.4, 1)
score_max_clipped_raw = log_loss(preds_df['label_binary'], preds_df['max_pred_clipped_raw'])
print('Score using average prediction of all frames all_c23.p: {:0.4f}'.format(score_avg23))
print('Score using minimum prediction of all frames all_c23.p: {:0.4f}'.format(score_min23))
print('Score using maximum prediction of all frames all_c23.p: {:0.4f}'.format(score_max23))
print('Score using 0.5 prediction of all frames: {:0.4f}'.format(score_naive))
print('Score using maximum clipped prediction of all frames: {:0.4f}'.format(score_max_clipped))
print('Score using average prediction of all frames all_raw.p: {:0.4f}'.format(score_avgraw))
print('Score using minimum prediction of all frames all_raw.p: {:0.4f}'.format(score_minraw))
print('Score using maximum prediction of all frames all_raw.p: {:0.4f}'.format(score_maxraw))
print('Score using maximum clipped prediction of all frames all_raw.p: {:0.4f}'.format(score_max_clipped_raw))
