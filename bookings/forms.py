from django import forms
from django.utils import timezone
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            "name",
            "email",
            "company",
            "event_name",
            "service_type",
            "number_of_people",
            "hours",
            "budget",
            "start_date",
            "end_date",
            "additional_notes",
        ]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control"}
            ),
            "company": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "event_name": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "service_type": forms.Select(
                attrs={"class": "form-select"}
            ),
            "number_of_people": forms.NumberInput(
                attrs={"class": "form-control", "min": 1}
            ),
            "hours": forms.NumberInput(
                attrs={"class": "form-control", "min": 1}
            ),
            "budget": forms.NumberInput(
                attrs={"class": "form-control", "min": 0, "step": "0.01"}
            ),
            "start_date": forms.DateInput(
                attrs={"class": "form-control", "type": "date"},
                format="%Y-%m-%d",
            ),
            "end_date": forms.DateInput(
                attrs={"class": "form-control", "type": "date"},
                format="%Y-%m-%d",
            ),
            "additional_notes": forms.Textarea(
                attrs={"class": "form-control", "rows": 4}
            ),
        }
        labels = {
            "number_of_people": "Number of people",
            "event_name": "Event name",
        }
        help_texts = {
            "hours": "Estimated hours per person.",
            "budget": "Total staffing budget (optional).",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["start_date"].input_formats = ["%Y-%m-%d"]
        self.fields["end_date"].input_formats = ["%Y-%m-%d"]

        today_iso = timezone.localdate().isoformat()
        self.fields["start_date"].widget.attrs["min"] = today_iso
        self.fields["end_date"].widget.attrs["min"] = today_iso

        placeholders = {
            "name": "Your name",
            "email": "you@example.com",
            "company": "Company or org",
            "event_name": "Event name",
            "budget": "e.g. 2500.00",
            "additional_notes": "Anything we should know…",
        }
        for field, text in placeholders.items():
            if field in self.fields:
                self.fields[field].widget.attrs.setdefault("placeholder", text)

    def clean(self):
        cleaned = super().clean()
        start = cleaned.get("start_date")
        end = cleaned.get("end_date")
        people = cleaned.get("number_of_people")
        hours = cleaned.get("hours")
        budget = cleaned.get("budget")

        if start and end and end < start:
            self.add_error(
                "end_date",
                "End date cannot be before the start date.",
            )
        if people is not None and people < 1:
            self.add_error(
                "number_of_people",
                "Please request at least one person.",
            )
        if hours is not None and hours < 1:
            self.add_error("hours", "Hours must be at least 1.")
        if budget is not None and budget < 0:
            self.add_error("budget", "Budget cannot be negative.")

        return cleaned
