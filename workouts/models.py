from django.db import models
from exercises.models import Exercise
from accounts.models import User
from django.core.validators import MaxValueValidator, MinValueValidator 

# Create your models here.

class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    workout_image_url = models.CharField(null=False, blank=True, default='')
    date_created = models.DateTimeField(auto_now_add=True)

class WorkoutExercise(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    sets = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    reps = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    weight = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
