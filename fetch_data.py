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
from sdk import *

IMG_PATH = os.path.join('datasets', 'plant_images')
IMG_URL=''
PROCESSED_PATH = os.path.join('datasets', 'processed')


def push_data(img_id= '', img_path=PROCESSED_PATH, img_obj=None, count=0):
    '''
    This function pushes a function to its designated folder locally 
    '''
    os.makedirs(img_path, exist_ok=True)
    save_path = os.path.join(img_path, f'{img_id}_{count}.jpg')
    cv2.imwrite(save_path, img_obj)
    return 0


def fetch_data(img_url=IMG_URL, img_path=IMG_PATH, filename="", f_log=None):
    '''
    This function fetches an img from the server and saves it in dataset folder
    '''
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

def fetch_overhead(jf_name):
    '''
    Opens all the files that keeps track of progress of the tool
    '''
    processed_log = open('fetched_log.json', 'r+')
    p_log = json.load(processed_log)
    json_file = open(jf_name)
    json_objs = json.load(json_file)
    return p_log, json_objs



def fetch_all():
    json_file_name = download_json_from_labelbox()
    f_log, json_objs = fetch_overhead(json_file_name)
    for index, obj in enumerate(json_objs):
        fetch_data(img_url=obj['Labeled Data'], img_path=IMG_PATH, filename=f'{obj["ID"]}', f_log=f_log)