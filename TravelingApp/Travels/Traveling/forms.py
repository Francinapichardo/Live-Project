from django.forms import ModelForm
from django import forms
from .models import Traveling


# Creates Account Form based on Traveling Model
class TravelingForm(ModelForm):
    class Meta:
        model = Traveling
        fields = '__all__'