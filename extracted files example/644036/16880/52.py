metadata['max_pred_c23'] = metadata['max_pred_c23'].round(6)
metadata.dropna(subset=['max_pred_c23']).sort_values('label')
