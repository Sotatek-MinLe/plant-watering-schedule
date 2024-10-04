import os
import django
import random
from datetime import datetime, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'plant_watering_schedule_api.settings')
django.setup()

from plant_watering_schedule.models import Plant


def create_plants():
    plants_data = [
        {'name': 'Aloe Vera', 'species': 'Aloe', 'watering_frequency_days': 7},
        {'name': 'Fiddle Leaf Fig', 'species': 'Ficus lyrata', 'watering_frequency_days': 14},
        {'name': 'Spider Plant', 'species': 'Chlorophytum comosum', 'watering_frequency_days': 10},
        {'name': 'Snake Plant', 'species': 'Sansevieria', 'watering_frequency_days': 14},
        {'name': 'Peace Lily', 'species': 'Spathiphyllum', 'watering_frequency_days': 7},
        {'name': 'Cactus', 'species': 'Cactaceae', 'watering_frequency_days': 30},
        {'name': 'Pothos', 'species': 'Epipremnum aureum', 'watering_frequency_days': 7},
        {'name': 'Rubber Plant', 'species': 'Ficus elastica', 'watering_frequency_days': 14},
        {'name': 'Orchid', 'species': 'Orchidaceae', 'watering_frequency_days': 10},
        {'name': 'Bamboo Plant', 'species': 'Bambusoideae', 'watering_frequency_days': 14},
    ]

    today = datetime.today().date()

    for plant_data in plants_data:
        plant = Plant(
            name=plant_data['name'],
            species=plant_data['species'],
            watering_frequency_days=plant_data['watering_frequency_days'],
            last_watered_date=today - timedelta(days=random.randint(0, 30))
        )
        plant.save()

    print(f"Add plant success")


if __name__ == '__main__':
    create_plants()
