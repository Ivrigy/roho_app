from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            "name",
            "company",
            "email",
            "event_name",
            "service_type",
            "number_of_people",
            "hours",
            "budget",
            "start_date",
            "end_date",
            "additional_notes",
        ]
