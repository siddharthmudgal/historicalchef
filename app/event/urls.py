from django.urls import include, path
from rest_framework import routers

from .api.views import EventViewSet, SearchEventViewSet

router = routers.DefaultRouter()
router.register('events', EventViewSet, basename='event')
router.register('search/event', SearchEventViewSet, basename='search-event')

app_name = 'event'

urlpatterns = [
    path('', include(router.urls)),
]
