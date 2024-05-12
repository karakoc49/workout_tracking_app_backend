from rest_framework import serializers
from .models import Exercise

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        # fields = '__all__'  # Include all fields for now (customize later)
        fields = ['id', 'name', 'description', 'muscle_group', 'gif_url']