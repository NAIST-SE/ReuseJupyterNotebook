def build_model():
    q_id = tf.keras.layers.Input((MAX_LEN,), dtype=tf.int32)
    q_type = tf.keras.layers.Input((MAX_LEN,), dtype=tf.int32)
    q_mask = tf.keras.layers.Input((MAX_LEN,), dtype=tf.int32)
    
    config = RobertaConfig.from_pretrained(PATH+'config-roberta-base.json')
    bert_model = TFRobertaModel.from_pretrained(PATH+'pretrained-roberta-base.h5',config=config)
    x = bert_model(q_id,attention_mask=q_mask,token_type_ids=q_type)
    
    x1 = tf.keras.layers.Dropout(0.2)(x[0])
    x1 = tf.keras.layers.GlobalAveragePooling1D()(x1)
    x1 = tf.keras.layers.Dense(3,'softmax')(x1)
    
    model = tf.keras.models.Model(inputs=[q_id, q_mask, q_type], outputs=x1)
    optimizer = tf.keras.optimizers.Adam(learning_rate=1e-5)
    model.compile(loss=tf.keras.losses.sparse_categorical_crossentropy, 
        optimizer=optimizer, metrics=['accuracy'])
    
    return model
