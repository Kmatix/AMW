from django.shortcuts import render
from rest_framework import viewsets
from .models import KartyGraficzne
from .serializers import KartySerializer

class KartyView(viewsets.ModelViewSet):
    queryset = KartyGraficzne.objects.all()
    serializer_class = KartySerializer
