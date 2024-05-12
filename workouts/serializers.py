from rest_framework import serializers

from exercises.serializers import ExerciseSerializer
from .models import Workout, WorkoutExercise

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        # fields = '__all__'  # Include all fields for now (customize later)
        fields = ['id', 'name', 'description', 'user', 'workout_image_url']

class WorkoutExerciseSerializer(serializers.ModelSerializer):
    exercise_data = ExerciseSerializer(source='exercise', read_only=True)
    class Meta:
        model = WorkoutExercise
        fields = ['id', 'workout', 'sets', 'reps', 'weight', 'exercise_data']