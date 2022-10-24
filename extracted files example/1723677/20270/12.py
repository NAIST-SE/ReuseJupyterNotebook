def serialize_example2(feature0, feature1, feature2, feature3, feature4, feature5): 
  feature = {
      'image': _bytes_feature(feature0),
      'image_name': _bytes_feature(feature1),
      'patient_id': _int64_feature(feature2),
      'sex': _int64_feature(feature3),
      'age_approx': _int64_feature(feature4),
      'anatom_site_general_challenge': _int64_feature(feature5),
  }
  example_proto = tf.train.Example(features=tf.train.Features(feature=feature))
  return example_proto.SerializeToString()
