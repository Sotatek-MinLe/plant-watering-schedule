from django.utils import timezone


# def now():
#     return timezone.now()


def today():
    return timezone.now().date()
