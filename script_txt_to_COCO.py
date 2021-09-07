import argparse
import glob
import os
import cv2
import json
import ast

data_dir = "/home/tobi/Documents/tirocinio_montini/immagini_montini_srl/2021-9-3_9-52-6/"
save_file = "/home/tobi/Documents/tirocinio_montini/immagini_montini_srl/2021-9-3_9-52-6/annotations/coco_annotations.json"

def create_json_object(data_dir):
    dict = {}
    dict["licenses"] = [{"name": "", "id": 0, "url": ""}]
    dict["info"] = {"contributor": "", "date_created": "", "description": "", "url": "", "version": "", "year": 2021}
    dict["categories"] = [{"id": 1, "name": "stop sign", "supercategory": ""}, {"id": 2, "name": "person", "supercategory": ""}]
    dict["images"] = []
    dict["annotations"] = []

    if data_dir[-1:] == '/':
        data_dir = data_dir[:-1]

    imgs = glob.glob(data_dir+'/*.jpg')
    id = 1
    for img in imgs:
        name = os.path.basename(img)
        cvimage = cv2.imread(img)
        dict["images"].append({"id": id, "width": cvimage.shape[1], "height": cvimage.shape[0], "file_name": name})
        id += 1

    id = 1
    for img in imgs:
        name = os.path.basename(img)
        code = name.replace(".jpg", "")
        code = code.replace("image", "")
        ann = glob.glob(data_dir + '/*[a-z]' + code + '.txt')
        print(code)
        print(ann)

        for annotazione in ann:
                for immagine in dict["images"]:
                    if name in immagine.values():
                        with open(annotazione) as f:
                            boxes = f.read().splitlines()
                            newboxes = []
                            for box in boxes:
                                newboxes.append(box.split(" "))
                            for box in newboxes:

                                if "pedestrian" in annotazione:
                                    category = 2
                                else:
                                    category = 1
                                area = float(box[2])*float(box[3])
                                stringa_box = ('[%s]' % ', '.join(map(str, box)))
                                dict["annotations"].append({"id": id,
                                                            "image_id": immagine["id"],
                                                            "category_id": category,
                                                            "segmentation": [],
                                                            "area": area,
                                                            "bbox": ast.literal_eval(stringa_box),
                                                            "iscrowd": 0,
                                                            "attributes": {"occluded": "false"}})

                                #dict["annotations"][id-1]["bbox"] = ast.literal_eval(dict["annotations"][id-1]["bbox"])

                                #dict["annotations"][id-1]["bbox"] = stringa_box

                                #print(dict["annotations"][id-1]["bbox"])
                                id += 1
    with open(save_file, 'w') as f:
        json.dump(dict, f)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Data Txt to Yolo')
    parser.add_argument('--data_dir', type=str, required=True, help='path of txt datas and images')
    parser.add_argument('--save_file', type=str, required=True, help='json file to save yolo data')
    parser.add_argument('--classes_file', type=list, required=True, help='txt file with the classes of the annotations, and the corrispondance ids')

    args = parser.parse_args()

    create_json_object(args.data_dir)

    #f = open("demofile.txt", "r")
    #print(f.read())
