from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


SERVICE_CHOICES = [
    ('power_hands', 'Power Hands'),
    ('security', 'Security'),
    ('promoters', 'Promoters'),
]

def no_past_date(value):
    if value < timezone.localdate():
        raise ValidationError("Cannot book past dates.")
    
# Create your models here.

