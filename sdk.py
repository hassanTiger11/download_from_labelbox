
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
        print(f'Downloaded labels already; return')
        return json_file_name
    LB_API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiJja3l1aXo5bDVoZ291MHo5MTZwdzgzcHRnIiwib3JnYW5pemF0aW9uSWQiOiJjazdtNWVrZXh4aGFkMDg2OG9nNmVxaHFyIiwiYXBpS2V5SWQiOiJjbDBjcGcwa3EwcWJjMHo1ZmdyMG5lb2s5Iiwic2VjcmV0IjoiYmE0OWRmNTdjNGFkNWUxNGEwZGYzOWNjOTQxNTIxMmEiLCJpYXQiOjE2NDY0MTU3NzcsImV4cCI6MjI3NzU2Nzc3N30.a709JWCGMJZdCScG-X6ilzZ3Wl6BQ5ZGhhkv3V4UglU"
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
