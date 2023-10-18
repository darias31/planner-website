from django.contrib import admin
from .models import Exercise, Workout, ExerciseInWorkout, MuscleCategory, Muscle

admin.site.register(Exercise)
admin.site.register(Workout)
admin.site.register(ExerciseInWorkout)
admin.site.register(MuscleCategory)
admin.site.register(Muscle)