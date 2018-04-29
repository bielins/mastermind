from django.shortcuts import render

from rest_framework.views import APIView

# Create your views here.

from rest_framework import generics

from . import models
from . import serializers


class GameList(generics.ListAPIView):
    queryset = models.Game.objects.all()
    serializer_class = serializers.GameSerializer


class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Game.objects.all()
    serializer_class = serializers.GameSerializer

class GameCreate(generics.CreateAPIView):
	queryset = models.Game.objects.all()
	serializer_class = serializers.GameCreateSerializer

