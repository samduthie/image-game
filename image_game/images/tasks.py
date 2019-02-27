from celery import Celery
import requests
import json

from images.models import Image, Tag
from images.keys import IMAGE_KEY

app = Celery('tasks', broker='pyamqp://guest@localhost//')

API_ADDRESS = 'https://vision.googleapis.com/v1/images:annotate?key={}'.format(IMAGE_KEY)


@app.task
def create_image_and_source_tags(url):
    image = create_image_as_model(url)
    get_tags_for_image(image)

@app.task
def create_image_as_model(url):
    return Image.objects.create(url=url)


@app.task
def get_tags_for_image(image):
    assert isinstance(image, Image)
    request_body = json.dumps({
        "requests": [
            {
                "image": {
                    "source": {
                        "imageUri": image.url
                    }
                },
                "features": [
                    {
                        "type": "LABEL_DETECTION",
                        "maxResults": 10
                    },
                    # {
                    #   "type": "WEB_DETECTION",
                    #   "maxResults": 2
                    # }
                ]
            }
        ]
    })

    headers = {
        "Content-Length": "3495",
        "Content-Type": "application/json"
    }

    response = requests.post(API_ADDRESS, request_body, headers=headers)
    resp_body = json.loads(response.text)

    tags = resp_body['responses'][0]['labelAnnotations']

    for tag in tags:
        description = tag.get('description')
        mid = tag.get('mid')
        score = tag.get('score')
        confidence = score

        Tag.objects.create(
            image=image,
            description=description,
            mid=mid,
            score=score,
            confidence=confidence
        )



