from celery import shared_task
from PIL import Image
import os
from django.conf import settings
from .models import Image as ImageModel

@shared_task
def process_image(image_id):
    instance = ImageModel.objects.get(id=image_id)
    image_path = instance.image.path

    try:
        image = Image.open(image_path)
        image = image.resize((800, 800))
        image.save(image_path)
    
    except Exception as e:
        pass
    
    instance.processed = True
    instance.save()
    