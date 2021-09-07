import glob
import os

data_dir = "/home/tobi/Documents/tirocinio_montini/dataset_1_6-09-2021-YOLO/"
with open(data_dir + 'train.txt', 'r') as f:
    immagini = f.read().splitlines()

immagini_da_tenere = []

with open('/home/tobi/Documents/tirocinio_montini/selection_images.txt', 'r') as f:
    listaimg = f.read().splitlines()

for img in listaimg:
    for c, immagine in enumerate(immagini):
        if 'image'+img+'.jpg' in immagine:
            immagini_da_tenere.append(immagine)

with open(data_dir + 'train.txt', 'w') as f:
    for i in immagini_da_tenere:
        f.write(i+'\n')


#cancello i file di testo e le immagini veri e propri

files = glob.glob(data_dir+'obj_train_data/image*.*')
for img in listaimg:
    for c, file in enumerate(files):
        if 'image'+img+'.' in file:
            del files[c]

for file in files:
    os.remove(file)