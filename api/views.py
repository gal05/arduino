from rest_framework import viewsets

from .models import Data
from .serializers import DataSerializer


class DataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all().order_by('id')
    serializer_class = DataSerializer

##
##class DataViewSetLluviaDetectada(viewsets.ModelViewSet):
##    queryset = Data.objects.raw("select * from data where sensor_lluvia like ('True')")
##    serializer_class = DataSerializer

##class DataViewSetLluviaNoDetectada(viewsets.ModelViewSet):
##    queryset = Data.objects.raw("select * from data where sensor_lluvia like ('False')")
##    serializer_class = DataSerializer
