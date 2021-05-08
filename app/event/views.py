from core.models import Event
from .serializers import EventSerializer

from rest_framework import viewsets


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
