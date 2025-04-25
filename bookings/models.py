from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from django.core.exceptions import ValidationError
import uuid


SERVICE_CHOICES = [
    ("power_hands", "Power Hands"),
    ("security", "Security"),
    ("promoters", "Promoters"),
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
    service_type = models.CharField(max_length=20, choices=SERVICE_CHOICES)
    number_of_people = models.PositiveIntegerField()
    hours = models.PositiveIntegerField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField(validators=[no_past_date])
    end_date = models.DateField(validators=[no_past_date])
    additional_notes = models.TextField(blank=True)
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(f"{self.name}-{self.start_date}")
            unique_id = uuid.uuid4().hex[:6]
            self.slug = f"{base_slug}-{unique_id}"
        super().save(*args, **kwargs)

    def can_edit(self):
        today = timezone.localdate()
        return today <= self.end_date and (self.start_date - today).days >= 10

    def __str__(self):
        return f"{self.get_service_type_display()} ({self.start_date}—{self.end_date})"
