from base64 import b64encode
import json
import requests

import cv2
import numpy as np

#from receipt_tracker.settings import GOOGLE_API_KEY
import os
GOOGLE_API_KEY = os.environ['GOOGLE_API_KEY']

ENDPOINT_URL = 'https://vision.googleapis.com/v1/images:annotate'
API_KEY = GOOGLE_API_KEY


def make_image_data_list(image_filenames):
    """
    image_filenames is a list of filename strings
    Returns a list of dicts formatted as the Vision API
        needs them to be
    """
    img_requests = []
    for imgname in image_filenames:
        with open(imgname, 'rb') as f:
            ctxt = b64encode(f.read()).decode()
            img_requests.append({
                'image': {'content': ctxt},
                'features': [{
                    'type': 'TEXT_DETECTION',
                    'maxResults': 1
                }]
            })
    return img_requests


def make_image_data(image_filenames):
    """Returns the image data lists as bytes"""
    imgdict = make_image_data_list(image_filenames)
    return json.dumps({"requests": imgdict}).encode()


def request_ocr(api_key, image_filenames):
    response = requests.post(ENDPOINT_URL,
                             data=make_image_data(image_filenames),
                             params={'key': api_key},
                             headers={'Content-Type': 'application/json'})
    return response


def get_text(file_content_byte):
    nparr = np.fromstring(file_content_byte, np.uint8)
    img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    kernel = np.ones((5, 5), np.uint8)
    img_eroded = cv2.erode(img_np, kernel, iterations=1)
    modified = cv2.imencode('.jpg', img_eroded)[1].tostring()

    ctxt = b64encode(modified).decode()
    #ctxt = b64encode(file_content_byte).decode()
    img_requests = [
        {
            'image': {'content': ctxt},
            'features': [{
                'type': 'TEXT_DETECTION',
                'maxResults': 1
            }]
        }
    ]
    data = json.dumps({"requests": img_requests}).encode()
    response = requests.post(ENDPOINT_URL,
                             data=data,
                             params={'key': API_KEY},
                             headers={'Content-Type': 'application/json'})

    if response.status_code != 200 or response.json().get('error'):
        return None
    else:
        return response.json()['responses'][0]


if __name__ == '__main__':
    image_filename = "test/test1.png"

    img = cv2.imread(image_filename, 0)
    _, img = cv2.threshold(img, 180, 255, cv2.THRESH_BINARY)

    kernel = np.ones((1, 15), np.uint8)
    img_eroded = cv2.erode(img, kernel, iterations=1)
    img_blurred = cv2.blur(img_eroded, (25, 1))
    _, img_blurred = cv2.threshold(img_blurred, 200, 255, cv2.THRESH_BINARY)

    cv2.imshow('Original', img_blurred)
    cv2.waitKey(0);
