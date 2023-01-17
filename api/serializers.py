from room.models import *
from sign.models import *
from django.contrib.auth.models import User
from rest_framework import serializers


class RoomSerializer(serializers.ModelSerializer):
    writer = serializers.PrimaryKeyRelatedField(queryset=Writer.objects.all(), many=True)

    class Meta:
        model = Room
        fields = ['writer', 'name']


class MessageSerializer(serializers.ModelSerializer):
    room = serializers.PrimaryKeyRelatedField(queryset=Room.objects.all())
    writer = serializers.PrimaryKeyRelatedField(queryset=Writer.objects.all())

    class Meta:
        model = Message
        fields = ['room', 'writer', 'text']
        extra_kwargs = {
            'writer': {'read_only': True},
        }

class WriterSerializer(serializers.ModelSerializer):
    writer = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Writer
        fields = ['writer', 'name', 'avatar']
        extra_kwargs = {
            'writer': {'read_only': True},
        }


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username']
        extra_kwargs = {
            'id': {'read_only': True},
            'username': {'read_only': True},
        }

