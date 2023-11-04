from django import forms
from django.forms import modelformset_factory, inlineformset_factory

from .models import Workout, ExerciseWithInfo

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['name', 'weekday']
        
class ExerciseWithInfoForm(forms.ModelForm):
    class Meta:
        model = ExerciseWithInfo
        fields = ['exercise','sets','reps','weight']

ExerciseWithInfoFormSet = inlineformset_factory(
    Workout,
    ExerciseWithInfo,
    form=ExerciseWithInfoForm,
    extra=3,
    can_delete=False,
)