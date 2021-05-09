from django.http import Http404
from rest_framework.decorators import action
from rest_framework.response import Response

from core.models import Event
from .serializers import EventSerializer

from rest_framework import viewsets
from ..services import service as service


class EventViewSet(viewsets.ModelViewSet):
    """view set for event"""
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    @action(methods=['POST'], detail=False)
    def find(self, request):
        """This REST API returns a set of events
        based on the search criteria"""
        event_search = request.data
        events = service.selectively_find_events(event_search)

        if events is None or len(events) == 0:
            raise Http404

        event_data = EventSerializer(events, many=True).data
        return Response(event_data)