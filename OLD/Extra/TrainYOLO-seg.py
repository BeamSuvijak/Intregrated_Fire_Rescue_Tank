


#install ultralytics
#install trainyolo-py

#DATASET PARAMETERS
API_KEY = "__FILL_IN_YOUR_API_KRY__"
PROJECT_NAME = "__FILL_IN_YOUR_PROJECT_NAME"

#YOLO PARAMETERS
IM_SIZE = 640
N_EPOCHS = 50 # you can lower this if you have a large dataset
BATCH_SIZE = 2 # you can increase this if you have a large dataset, > 50 images, you can increase this to 4, > 100 images you can increase this to 8
MODEL = 'yolov8n-seg.pt'

from trainyolo.client import Client, Project

#init client
client = Client(API_KEY)

# Load Project
project = Project.get_by_name(client, PROJECT_NAME)
project_location = project.pull(location='./data', format='yolov8')

# Train yolo model


