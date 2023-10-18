from django.db import models
import uuid

class MuscleCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Muscle(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(MuscleCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Exercise(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    primary_muscle = models.ManyToManyField(Muscle, related_name='primary_exercises')
    secondary_muscle = models.ManyToManyField(Muscle, related_name='secondary_exercises')

    def __str__(self):
        return self.name
    
class Workout(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    weekday = models.CharField(max_length=20)
    exercises = models.ManyToManyField(Exercise, through='ExerciseInWorkout')

    def __str__(self):
        return self.name

class ExerciseInWorkout(models.Model):
    id = models.AutoField(primary_key=True)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    sets = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.exercise.name} in {self.workout.name}'


