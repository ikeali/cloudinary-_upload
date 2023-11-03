from django.db import models
from cloudinary.models import CloudinaryField




class Image(models.Model):
    title = models.CharField(max_length=255)
    file = CloudinaryField('image')

