import io, os
from google.cloud import vision
from google.cloud.vision import types

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"ServiceAccToken.json"

client = vision.ImageAnnotatorClient()

FILE_NAME = 'text1.jpg'
FOLDER_PATH = r'C:\Personal\Miscellaneous\Coding_things\VisionAPIDemo\Images'

with io.open(os.path.join(FOLDER_PATH, FILE_NAME), 'rb') as image_file:
    content = image_file.read()

image = vision.types.Image(content=content)

response = client.text_detection(image=image)