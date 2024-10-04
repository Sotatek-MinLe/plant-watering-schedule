from django.db import models


# Create your models here.

class Plant(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    species = models.CharField(max_length=100, blank=False)
    watering_frequency_days = models.PositiveIntegerField(null=False, default=0)
    last_watered_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name
