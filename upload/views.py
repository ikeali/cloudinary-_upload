from django.shortcuts import render
from rest_framework import viewsets
from .models import Image
from .serializers import ImageSerializer

# from django.conf import settings
# import os
# import cloudinary


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer



    # def __init__(self, *args, **kwargs):
    #     super(ImageViewSet, self).__init__(*args, **kwargs)
    #     cloudinary.config(
    #         cloud_name='dshmzjuro',  # Use the cloud_name from the CLOUDINARY_URL
    #         api_key='792831766247376',  # Use the API key from the CLOUDINARY_URL
    #         api_secret='waHWSGvoLSnKPTbqh3W8HxYpooA',  # Use the API secret from the CLOUDINARY_URL
    #     )