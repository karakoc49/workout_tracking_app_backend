from django.contrib import admin
from .models import Workout, WorkoutExercise
# Register your models here.

admin.site.register(Workout)
admin.site.register(WorkoutExercise)

