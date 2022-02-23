#this file fetches the data for this project
#The data is California census from 1999
#This script will help automize the process and 
#set up for regular fetching
import os
import tarfile
from PIL import Image
import urllib.request 
import cv2
import json

IMG_PATH = os.path.join('datasets', 'plant_images')
IMG_URL = 'https://storage.labelbox.com/ck7m5ekexxhad0868og6eqhqr%2F6c0c1d63-d05a-59c3-221b-62cf1c215259-78ac8a19-e76a-42af-9983-b47cc0de8832_rawData0046.png?Expires=1646346539574&KeyName=labelbox-assets-key-3&Signature=zXUR3KN7R73n6BlLQ3j6i9H-VPI'

PROCESSED_PATH = os.path.join('datasets', 'processed')
EDGE_PLANT = os.path.join(PROCESSED_PATH, "edge_plant")
WHOLE_PLANT = os.path.join(PROCESSED_PATH, "whole_plant")
def push_data(img_id= '', img_path=PROCESSED_PATH, img_obj=None, count=0):
    os.makedirs(img_path, exist_ok=True)
    save_path = os.path.join(img_path, f'{img_id}_{count}.jpg')
    cv2.imwrite(save_path, img_obj)
    return 0


def fetch_data(img_url=IMG_URL, img_path=IMG_PATH, filename="", f_log=None):
    print(f'--------------fetch images------------')
    filename+='.jpg' #concat extension
    os.makedirs(img_path, exist_ok=True)
    img_name = os.path.join(IMG_PATH, filename)
    print(f'fetching: {img_name}')
    if(filename in f_log): 
        print(f'already exist: {filename}')
        return
    urllib.request.urlretrieve(img_url, img_name)
    
    f_log.append(filename)
    json.dump(f_log, open('fetched_log.json', 'r+'), indent=2)

def fetch_overhead():
    processed_log = open('fetched_log.json', 'r+')
    p_log = json.load(processed_log)
    return p_log

json_file = open('labels.json')
json_objs = json.load(json_file)
def main():  
    f_log = fetch_overhead()
    for index, obj in enumerate(json_objs):
        fetch_data(img_url=obj['Labeled Data'], img_path=IMG_PATH, filename=f'{obj["ID"]}', f_log=f_log)

if __name__ == '__main__':
    main()