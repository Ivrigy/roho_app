from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify


SERVICE_CHOICES = [
    ('power_hands', 'Power Hands'),
    ('security', 'Security'),
    ('promoters', 'Promoters'),
]

def no_past_date(value):
    if value < timezone.localdate():
        raise ValidationError("Cannot book past dates.")
    
# Create your models here.

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100, blank=True)
    email = models.EmailField()
    event_name = models.CharField(max_length=100)
    service_type = models.CharField(max_length=20,choices=SERVICE_CHOICES)
    number_of_people = models.PositiveIntegerField()
    start_date = models.DateField(validators=[no_past_date])
    end_date = models.DateField(validators=[no_past_date])
    additional_notes = models.TextField(blank=True)
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    
    
