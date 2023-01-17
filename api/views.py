
from rest_framework import viewsets
from django.shortcuts import Http404
from rest_framework.response import Response


from room.models import *
from sign.models import *
from .serializers import *
from django.contrib.auth.models import User


class RoomlViewset(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class MessageViewset(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def perform_create(self, serializer):
        serializer.save(writer=Writer.objects.get(writer=self.request.user))


class WriterViewset(viewsets.ModelViewSet):
    queryset = Writer.objects.all()
    serializer_class = WriterSerializer

    def perform_create(self, serializer):
        serializer.save(writer=self.request.user)


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request):
        queryset = [User.objects.get(id=request.user.id)]
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

