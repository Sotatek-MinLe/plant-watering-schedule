from django.urls import reverse
from django.test import TestCase
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APIClient

from .models import Plant


# Create your tests here.

class PlantTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.plant = Plant.objects.create(
            name="Fern",
            species="Pteridophyta",
            watering_frequency_days=7,
            last_watered_date=None,
        )

    def test_plan_watering(self):
        response = self.client.patch(
            reverse("plant-watering", kwargs={"pk": self.plant.pk})
        )
        self.plant.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(self.plant.last_watered_date)
        self.assertEqual(self.plant.last_watered_date, timezone.now().date())
