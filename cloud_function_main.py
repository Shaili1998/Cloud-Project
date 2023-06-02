
import requests
from io import BytesIO
import numpy as np
import pandas as pd
import tensorflow as tf
import os
from google.cloud import storage
from google.cloud import aiplatform
from PIL import Image 
from tensorflow.keras.preprocessing.image import load_img, img_to_array, array_to_img

def change_size(image):
    img = array_to_img(image, scale=False) #returns PIL Image
    img = img.resize((75, 75)) #resize image
    img = img.convert(mode='RGB') #makes 3 channels
    arr = img_to_array(img) #convert back to array
    return arr.astype(np.float64)

# Define endpoint
aip_endpoint_name = (
    f"projects/591498791142/locations/us-central1/endpoints/6694921903481552896"
)

endpoint = aiplatform.Endpoint(aip_endpoint_name)

        
# Main entry point for the cloud function
def hello_world(request):

    
    params = request.get_json()

    if (params is not None) and ('url' in params):

        url = params['url']
        print(url)

        # get image from response url  and preprocess image
        response = requests.get(url)
        img = Image.open(BytesIO(response.content)).convert('L')
        img = np.array(img)

        test_arr = np.array(img).reshape(-1, 28, 28, 1)

        test_arr_75 = [change_size(img) for img in test_arr]
        test_arr_75 = np.array(test_arr_75)
        
        # predict using endpoint and return ans
        ans = np.argmax(endpoint.predict(test_arr_75.tolist()).predictions)

        print(ans)

        return str(ans)
        
    else:
        return "nothing sent for prediction"
