
# install latest labelbox version
import labelbox

# Enter your Labelbox API key here
LB_API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiJja3l1aXo5bDVoZ291MHo5MTZwdzgzcHRnIiwib3JnYW5pemF0aW9uSWQiOiJjazdtNWVrZXh4aGFkMDg2OG9nNmVxaHFyIiwiYXBpS2V5SWQiOiJja3pyZnp2MWoyMnphMHo5bzFhbnNiNTF0Iiwic2VjcmV0IjoiZGI4MjE5ZDJlNmM4ZGI1NjBmM2NhYjFlNDIxMWRjZWIiLCJpYXQiOjE2NDUxMzAxMTcsImV4cCI6MjI3NjI4MjExN30.iYzP-3j-2iwrZmm-aWT3Da-a_18orVPKOBbo29Vj1nc"
# Create Labelbox client
lb = labelbox.Client(api_key=LB_API_KEY)
# Get project by ID
project = lb.get_project('ckz5pxc9r6fc70z97a35hc3f6')
# Export image and text data as an annotation generator:
labels = project.label_generator()
# Export video annotations as an annotation generator:
labels = project.video_label_generator()
# Export labels created in the selected date range as a json file:
labels = project.export_labels(download = True, start="2022-02-11", end="2022-02-17")