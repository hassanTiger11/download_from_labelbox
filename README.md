# download_from_labelbox


This tool help download a set of images from label box and use the labels to mask those images. The tool put each masked image under its label

## Before using
create a virtual environment and install requirements
`virtualenv .venv`
`pip install -r requirements.txt`

## Usage
please change LB_API_KEY in sdk.py to your Label box api key then run main.py
`python3 main.py`