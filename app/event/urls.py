from django.urls import include, path
from rest_framework import routers

from .api.views import EventViewSet

router = routers.DefaultRouter()
router.register('events', EventViewSet, basename='event')


app_name = 'event'

urlpatterns = [
    path('', include(router.urls))
]
