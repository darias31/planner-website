from django.db import models
import uuid

class Exercise(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    name = models.CharField(max_length=100)
    primary_muscle = models.CharField(max_length=100)
    secondary_muscle = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class Workout(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    name = models.CharField(max_length=100)
    weekday = models.CharField(max_length=20)
    exercises = models.ManyToManyField(Exercise, through='ExerciseInWorkout')

    def __str__(self):
        return f"{self.weekday} - {self.name}"

class ExerciseInWorkout(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    sets = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.exercise.name} - Sets: {self.sets}, Reps: {self.reps}"


