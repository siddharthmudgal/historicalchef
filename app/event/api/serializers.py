from rest_framework import serializers
from core.models import Event


class EventSerializer(serializers.ModelSerializer):
    """Serializer class for events"""

    class Meta:
        model = Event
        fields = ('created_at', 'email', 'environment', 'component',
                  'message', 'data_payload')


class SearchEventSerializer(serializers.Serializer):
    """serializer class for search"""

    created_at = serializers.CharField(allow_blank=True)
    email = serializers.EmailField(allow_blank=True)
    environment = serializers.CharField(allow_blank=True)
    component = serializers.CharField(allow_blank=True)
    message = serializers.CharField(allow_blank=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
