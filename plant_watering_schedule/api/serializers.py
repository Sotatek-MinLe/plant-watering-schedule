from rest_framework import serializers
from plant_watering_schedule.models import Plant
from utils import time_util


class PlantSerializer(serializers.ModelSerializer):
    today_watered = serializers.SerializerMethodField()

    class Meta:
        model = Plant
        exclude = ('id',)

    def get_today_watered(self, obj):
        return obj.last_watered_date is not None and obj.last_watered_date == time_util.today()

    # def validate_name(self, value):
    #     if Plant.objects.filter(name=value).exists():
    #         raise serializers.ValidationError("This name is already taken")
    #     return value

