from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
import sys
import time
from dotenv import load_dotenv
load_dotenv()
import os

subscription_key = os.getenv('SUBSCRIPTION_KEY')
endopoint = os.getenv('ENDPOINT')
computervision_client = ComputerVisionClient(endopoint, CognitiveServicesCredentials(subscription_key))

remote_image_url = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-sample-data-files/master/ComputerVision/Images/landmark.jpg"

def detective():
    '''
    Detect Brands - remote
    This example detects common brands like logos and puts a bounding box around them.
    '''
    print("===== Detect Brands - remote =====")
    # Get a URL with a brand logo
    # remote_image_url = "https://storageaccountankir99ce.blob.core.windows.net/images/chanel.jpg"
    remote_image_url = "https://storageaccountankir99ce.blob.core.windows.net/images/IMG_9153.PNG"
    
    # Select the visual feature(s) you want
    remote_image_features = ["brands"]
    
    # Call API with URL and features
    detect_brands_results_remote = computervision_client.analyze_image(remote_image_url, remote_image_features)
    hoge = ''
    print("Detecting brands in remote image: ")
    if len(detect_brands_results_remote.brands) == 0:
        print("No brands detected.")
    else:
        for brand in detect_brands_results_remote.brands:
            hoge = "'{}' brand detected with confidence {:.1f}% at location {}, {}, {}, {}".format( \
            brand.name, brand.confidence * 100, brand.rectangle.x, brand.rectangle.x + brand.rectangle.w, \
            brand.rectangle.y, brand.rectangle.y + brand.rectangle.h)
            print(hoge)
    # return hoge

detective()