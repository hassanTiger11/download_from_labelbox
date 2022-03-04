
# install latest labelbox version
import labelbox
import json
import os
# Enter your Labelbox API key here
def download_json_from_labelbox():
    '''
    Downloads labels from labelsbox
    Change LB_API_KEY before using
    '''
    json_file_name = 'labels.json'
    if(os.path.exists(os.path.join(os.getcwd(), json_file_name))):
        if(json.load(open(json_file_name)) != []):
            print(f'SDK: Already downloaded labels; return')
            return json_file_name
    LB_API_KEY = ""
    # Create Labelbox client
    lb = labelbox.Client(api_key=LB_API_KEY)
    # Get project by ID
    project = lb.get_project('ckz5pxc9r6fc70z97a35hc3f6')
    # Export image and text data as an annotation generator:
    labels = project.label_generator()
    # Export video annotations as an annotation generator:
    #labels = project.video_label_generator()
    # Export labels created in the selected date range as a json file:
    labels = project.export_labels(download = True, start="2022-01-24", end="2022-02-17")

    
    file = open(json_file_name, 'w+')
    json.dump(labels, file, indent=2)
    return json_file_name
