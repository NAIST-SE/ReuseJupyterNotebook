import numpy as np, pandas as pd, os, time, gc
import xml.etree.ElementTree as ET , time
import matplotlib.pyplot as plt, zipfile 
from PIL import Image 

# STOP KERNEL IF IT RUNS FOR MORE THAN 8 HOURS
kernel_start = time.time()
LIMIT = 8

# PREPROCESS IMAGES
ComputeLB = True
DogsOnly = True
ROOT = '../input/generative-dog-images/'
if not ComputeLB: ROOT = '../input/'
IMAGES = os.listdir(ROOT + 'all-dogs/all-dogs/')
breeds = os.listdir(ROOT + 'annotation/Annotation/') 

idxIn = 0; namesIn = []
imagesIn = np.zeros((25000,80,80,3))

# CROP WITH BOUNDING BOXES TO GET DOGS ONLY
# https://www.kaggle.com/paulorzp/show-annotations-and-breeds
if DogsOnly:
    for breed in breeds:
        for dog in os.listdir(ROOT+'annotation/Annotation/'+breed):
            try: img = Image.open(ROOT+'all-dogs/all-dogs/'+dog+'.jpg') 
            except: continue           
            ww,hh = img.size
            tree = ET.parse(ROOT+'annotation/Annotation/'+breed+'/'+dog)
            root = tree.getroot()
            objects = root.findall('object')
            for o in objects:
                bndbox = o.find('bndbox') 
                xmin = int(bndbox.find('xmin').text)
                ymin = int(bndbox.find('ymin').text)
                xmax = int(bndbox.find('xmax').text)
                ymax = int(bndbox.find('ymax').text)
                w = np.min((xmax - xmin, ymax - ymin))
                # ADD PADDING TO CROPS
                EXTRA = w//8
                a1 = EXTRA; a2 = EXTRA; b1 = EXTRA; b2 = EXTRA
                a1 = np.min((a1,xmin)); a2 = np.min((a2,ww-xmin-w))
                b1 = np.min((b1,ymin)); b2 = np.min((b2,hh-ymin-w))
                img2 = img.crop((xmin-a1, ymin-b1, xmin+w+a2, ymin+w+b2))
                img2 = img2.resize((80,80), Image.ANTIALIAS)
                imagesIn[idxIn,:,:,:] = np.asarray(img2)
                namesIn.append(breed)                
                #if idxIn%1000==0: print(idxIn)
                idxIn += 1
                
    idx = np.arange(idxIn)
    np.random.shuffle(idx)
    imagesIn = imagesIn[idx,:,:,:]
    namesIn = np.array(namesIn)[idx]
    
# RANDOMLY CROP FULL IMAGES
else:
    for k in range(len(IMAGES)):
        img = Image.open(ROOT + 'all-dogs/all-dogs/' + IMAGES[k])
        w = img.size[0]
        h = img.size[1]
        sz = np.min((w,h))
        a=0; b=0
        if w<h: b = (h-sz)//2
        else: a = (w-sz)//2
        img = img.crop((0+a, 0+b, sz+a, sz+b))  
        img = img.resize((64,64), Image.ANTIALIAS)   
        imagesIn[idxIn,:,:,:] = np.asarray(img)
        namesIn.append(IMAGES[k])               
        #if (idxIn%1000==0): print(idxIn)
        idxIn += 1 
    
# DISPLAY CROPPED IMAGES
x = np.random.randint(0,idxIn,25)
for k in range(3):
    plt.figure(figsize=(15,3))
    for j in range(5):
        plt.subplot(1,5,j+1)
        img = Image.fromarray( imagesIn[x[k*5+j],:,:,:].astype('uint8') )
        plt.axis('off')
        if not DogsOnly: plt.title(namesIn[x[k*5+j]],fontsize=11)
        else: plt.title(namesIn[x[k*5+j]].split('-')[1],fontsize=11)
        plt.imshow(img)
    plt.show()
