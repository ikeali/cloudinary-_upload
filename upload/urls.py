from rest_framework import routers
from .views import ImageViewSet
from django.urls import path, include


router = routers.DefaultRouter()
router.register(r'images', ImageViewSet)

urlpatterns = [
    # ... your other URL patterns ...
    path('', include(router.urls)),
]