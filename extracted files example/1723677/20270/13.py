SIZE = 687
CT = len(IMGS2)//SIZE + int(len(IMGS2)%SIZE!=0)
for j in range(CT):
    print(); print('Writing TFRecord %i of %i...'%(j,CT))
    CT2 = min(SIZE,len(IMGS2)-j*SIZE)
    with tf.io.TFRecordWriter('test%.2i-%i.tfrec'%(j,CT2)) as writer:
        for k in range(CT2):
            img = cv2.imread(PATH2+IMGS2[SIZE*j+k])
            img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR) # Fix incorrect colors
            img = cv2.imencode('.jpg', img, (cv2.IMWRITE_JPEG_QUALITY, 94))[1].tostring()
            name = IMGS2[SIZE*j+k].split('.')[0]
            row = test.loc[test.image_name==name]
            example = serialize_example2(
                img, str.encode(name),
                row.patient_id.values[0],
                row.sex.values[0],
                row.age_approx.values[0],                        
                row.anatom_site_general_challenge.values[0])
            writer.write(example)
            if k%100==0: print(k,', ',end='')
