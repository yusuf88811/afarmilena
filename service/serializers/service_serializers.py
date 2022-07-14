from rest_framework import serializers

from service.models import Service
from service.serializers.events_serializers import EventSerializers


class ServiceSerializers(serializers.ModelSerializer):
    # events = EventSerializers(source='events_set', many=True, read_only=True)

    class Meta:
        model = Service
        fields = ["id", "name", "type", "price", "image", "video", "description", "event"]
