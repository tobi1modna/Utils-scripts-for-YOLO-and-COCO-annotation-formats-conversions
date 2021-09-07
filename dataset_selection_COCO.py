import glob
import json
import os

data_dir = "/home/tobi/Documents/tirocinio_montini/dataset_1_6-09-2021/"
with open(data_dir + 'annotations/instances_default.json', 'r') as f:
    dict = json.load(f)

with open(data_dir + 'selection_images.txt', 'r') as f:
    listaimg = f.read().splitlines()

immagini_da_cancellare = glob.glob(data_dir+'images/*.jpg')
for immagine_da_tenere in listaimg:
    img = glob.glob(data_dir+'images/image'+immagine_da_tenere+'.jpg')
    immagini_da_cancellare.remove(img[0])

for c, img in enumerate(immagini_da_cancellare):
    os.remove(img)
    immagini_da_cancellare[c] = img.replace(data_dir+'images/', '')

for immagine in immagini_da_cancellare:
    for c, image in enumerate(dict["images"]):
        if image["file_name"] == immagine:
            print(immagine)
            del dict["images"][c]
ids = []
for image in dict["images"]:
    ids.append(image["id"])

for c, ann in enumerate(dict["annotations"]):
    if ann["image_id"] not in ids:
        del dict["annotations"][c]

with open(data_dir+'annotations/coco_annotations.json', 'w') as f:
    json.dump(dict, f)
