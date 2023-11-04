from django.db import models


class MuscleCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Muscle(models.Model):
    muscle_category = models.ForeignKey(MuscleCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Exercise(models.Model):
    muscle = models.ManyToManyField(Muscle)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Workout(models.Model):
    name = models.CharField(max_length=100)
    weekday = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class ExerciseWithInfo(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    workout = models.ForeignKey(
        "Workout", on_delete=models.CASCADE, related_name="exercise_with_info_set"
    )
    sets = models.PositiveIntegerField(default=0)
    reps = models.PositiveIntegerField(default=0)
    weight = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.exercise.name} in {self.workout.name}"
