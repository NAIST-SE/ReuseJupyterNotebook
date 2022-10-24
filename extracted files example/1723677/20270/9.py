def serialize_example(feature0, feature1, feature2, feature3, feature4, feature5, feature6, feature7):
  feature = {
      'image': _bytes_feature(feature0),
      'image_name': _bytes_feature(feature1),
      'patient_id': _int64_feature(feature2),
      'sex': _int64_feature(feature3),
      'age_approx': _int64_feature(feature4),
      'anatom_site_general_challenge': _int64_feature(feature5),
      'source': _int64_feature(feature6),
      'target': _int64_feature(feature7)
  }
  example_proto = tf.train.Example(features=tf.train.Features(feature=feature))
  return example_proto.SerializeToString()
