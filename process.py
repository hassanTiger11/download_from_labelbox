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

def process_overhead():
    processed_log = open('processed_log.json', 'r+')
    p_log = json.load(processed_log)
    return p_log

def process(i, p_log):
    print(f'--------------Processes images------------')
    

    obj = json_objs[i]
    
    if(f'{obj["ID"]}.jpg' in p_log):
        print(f'Process: already processed {obj["ID"]}.jpg')
        return 

    img_path = os.path.join(IMG_PATH, f'{obj["ID"]}.jpg')
    abs_img_path = os.path.abspath(img_path)
    print(f'Processing: {abs_img_path}')
    img = cv2.imread(abs_img_path)
    if (not type(img) is np.ndarray):
        print("cv2: couldn't find image")
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
        if(value == "whole_plant"):
            push_data(img_id= obj["ID"], img_path=WHOLE_PLANT, img_obj=masked, count=index)
        elif(value == "edge_plant"):
            push_data(img_id= obj["ID"], img_path=EDGE_PLANT, img_obj=masked, count=index)
        else:
            push_data(img_id= obj["ID"], img_path=PROCESSED_PATH, img_obj=masked, count=index)

    p_log.append(f'{obj["ID"]}.jpg' )
    json.dump(p_log, open('processed_log.json', 'w+'), indent=2)
    
    #remove all sides but the box
def main():
    p_log = process_overhead()  
    for index, obj in enumerate(json_objs):
        process(index, p_log=p_log)
        
if __name__ == '__main__':
    main()