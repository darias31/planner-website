from django.contrib import admin
from .models import Exercise, Workout, ExerciseInWorkout

admin.site.register(Exercise)
admin.site.register(Workout)
admin.site.register(ExerciseInWorkout)