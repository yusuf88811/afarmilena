from rest_framework import serializers

from service.models.booked_dates import BookedDates


class BookedDetSerializers(serializers.ModelSerializer):
    class Meta:
        model = BookedDates
        fields = ["id", "date", "wedding_hall"]
