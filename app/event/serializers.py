from rest_framework import serializers
from core.models import Event


class EventSerializer(serializers.ModelSerializer):
    """Serializer class for events"""

    class Meta:
        model = Event
        fields = ('created_at', 'email', 'environment', 'component',
                  'message', 'data_payload')


class EventSearchSerializer(serializers.Serializer):
    """Serializer class for events"""

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    created_at = serializers.IntegerField(default=1)
    email = serializers.CharField(default='')
    environment = serializers.CharField(default='')
    component = serializers.CharField(default='')
    message = serializers.CharField(default='')
