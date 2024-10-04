from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from plant_watering_schedule.api.serializers import PlantSerializer
from plant_watering_schedule.models import Plant
from utils import time_util


# Create your views here.

class PlantViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet
                   ):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer

    @action(detail=True, methods=['patch'])
    def watering(self, request, pk=None):
        plant = self.get_object()
        plant.last_watered_date = time_util.today()
        plant.save()

        return Response(
            {"status": "OK"},
            status=status.HTTP_200_OK
        )
