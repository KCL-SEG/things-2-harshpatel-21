"""Forms of the project."""

# Create your forms here.
from typing import Any
from django import forms
from django.contrib.auth import authenticate
from django.core.validators import RegexValidator
from django.core.exceptions import ObjectDoesNotExist
from things.models import Thing

class ThingForm(forms.ModelForm):
    
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']

        widgets = {
        'description': forms.Textarea(),
        'quantity': forms.NumberInput(),
        }
    
    def save(self):
        """Save the provided password in hashed format."""
        super().clean()
        thing = super().save(commit=False)
        thing.save()
        return thing