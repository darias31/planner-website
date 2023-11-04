from django.contrib import admin
from .models import MuscleCategory, Muscle, Exercise, ExerciseWithInfo, Workout

admin.site.register(Exercise)
admin.site.register(Workout)
admin.site.register(MuscleCategory)
admin.site.register(Muscle)
admin.site.register(ExerciseWithInfo)