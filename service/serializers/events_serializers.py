from rest_framework import serializers

from service.models.events import Event
from service.serializers.wedding_hall_serializers import WeddingHallSerializers


class EventSerializers(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ['id', 'name', 'image', 'active', 'description']
