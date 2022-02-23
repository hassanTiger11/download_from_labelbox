import json
from fetch_data import *
import numpy as np
import cv2
import sys



def get_obj_str(i, obj=json_objs):
    formatted = json.dumps(obj[i], indent=2)
    #print(formatted)
    return formatted

def process_overhead():
    json_file = open('labels.json')
    json_objs = json.load(json_file)
    processed_log = open('processed_log.json', 'r+')
    p_log = json.load(processed_log)
    return p_log, json_objs

def process(i, p_log={}, json_objs={}):
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
    if(obj["Label"] == {}):
        print(f'processes: {obj["ID"]} has no labels; moving next')
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
    
def process_by_id(ID = "", p_log={}, json_objs={}):
    if(ID == ""): return
    p_log, json_objs = process_overhead()  
    for index, obj in enumerate(json_objs):
        if(f'{obj["ID"]}.jpg' == ID):
            print(f'process by id: processing {ID}')
            process(index, p_log=p_log, json_objs=json_objs)

def process_all():
    p_log, json_objs = process_overhead()  
    for index, obj in enumerate(json_objs):
        process(index, p_log=p_log)
    
def main():
    not_processed = open('not_processed', 'r+')
    p_log, json_objs = process_overhead()
    np_json = json.load(not_processed)
    for id in np_json:
        process_by_id(ID=id, p_log=p_log, json_objs=json_objs)
        
if __name__ == '__main__':
    main()
