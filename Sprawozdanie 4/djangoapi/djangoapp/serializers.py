from rest_framework import serializers
from .models import KartyGraficzne

class KartySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = KartyGraficzne
        fields = ('id', 'url', 'name', 'price')