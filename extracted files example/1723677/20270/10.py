SIZE = 2071
CT = len(IMGS)//SIZE + int(len(IMGS)%SIZE!=0)
for j in range(CT):
    print(); print('Writing TFRecord %i of %i...'%(j,CT))
    CT2 = min(SIZE,len(IMGS)-j*SIZE)
    with tf.io.TFRecordWriter('train%.2i-%i.tfrec'%(j,CT2)) as writer:
        for k in range(CT2):
            img = cv2.imread(PATH+IMGS[SIZE*j+k])
            img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR) # Fix incorrect colors
            img = cv2.imencode('.jpg', img, (cv2.IMWRITE_JPEG_QUALITY, 94))[1].tostring()
            name = IMGS[SIZE*j+k].split('.')[0]
            row = df.loc[df.image_name==name]
            example = serialize_example(
                img, str.encode(name),
                row.patient_id.values[0],
                row.sex.values[0],
                row.age_approx.values[0],                        
                row.anatom_site_general_challenge.values[0],
                row.source.values[0],
                row.target.values[0])
            writer.write(example)
            if k%100==0: print(k,', ',end='')
