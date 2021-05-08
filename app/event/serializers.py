from rest_framework import serializers
from core.models import Event


class EventSerializer(serializers.ModelSerializer):
    """Serializer class for events"""

    class Meta:
        model = Event
        fields = ('created_at', 'email', 'environment', 'component',
                  'message', 'data_payload')
