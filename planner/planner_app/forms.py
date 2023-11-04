from django import forms
from django.forms import modelformset_factory

from .models import Workout

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['name', 'weekday']
        