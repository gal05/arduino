from rest_framework import serializers
from .models import Data


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ('id', 'humedad', 'temperatura', 'rayos_v', 'sensor_lluvia', 'created_at')