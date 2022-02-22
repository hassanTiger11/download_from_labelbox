import json
from fetch_data import *
import numpy as np
import cv2
import sys
json_file = open('labels.json')
json_objs = json.load(json_file)


def get_obj_str(i, obj=json_objs):
    formatted = json.dumps(obj[i], indent=2)
    #print(formatted)
    return formatted


def process(i):
    obj = json_objs[i]
    #get the image intor dir
    fetch_data(img_url=obj['Labeled Data'], img_path=IMG_PATH, filename=f'{obj["ID"]}.jpg')
    
    img_path = os.path.join(IMG_PATH, f'{obj["ID"]}.jpg')
    abs_img_path = os.path.abspath(img_path)
    print(f'Processing: {abs_img_path}', file=sys.stderr)
    img = cv2.imread(abs_img_path)
    if (not type(img) is np.ndarray):
        print("cv2: couldn't find image", file=sys.stderr)
        return
    
    labels = obj["Label"]["objects"]
    #dimenstions of mask
    for index, label in enumerate(labels):
        print(f'label = {label}')   
        value = label['value']
        top = (label['bbox']["top"])
        left = int(label['bbox']["left"])
        width = int(label['bbox']["width"])
        height = int(label['bbox']["height"])
        mask = np.zeros(img.shape[:2], dtype="uint8")
        cv2.rectangle(mask, (left, top), (left+width, top+height), 255, -1)
        masked = cv2.bitwise_and(img, img, mask=mask)
        #save this file 
        push_data(img_id= obj["ID"], img_path=PROCESSED_PATH, img_obj=masked, count=index)
        #cv2.imshow("Mask Applied to Image", masked)
        #cv2.waitKey()

    #remove all sides but the box

process(0)
    
