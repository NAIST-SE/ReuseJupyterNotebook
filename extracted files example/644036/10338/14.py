opacity = detailed_class_info \
    .loc[detailed_class_info['class'] == 'Lung Opacity'] \
    .reset_index()
not_normal = detailed_class_info \
    .loc[detailed_class_info['class'] == 'No Lung Opacity / Not Normal'] \
    .reset_index()
normal = detailed_class_info \
    .loc[detailed_class_info['class'] == 'Normal'] \
    .reset_index()
