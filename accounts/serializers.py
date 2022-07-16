from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import CustomUser, BlockList
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'phone', 'cite', 'wedding_date']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)


class BlockListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlockList
        fields = ["reason", "user"]
