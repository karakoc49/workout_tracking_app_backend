from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response

from .models import Workout, WorkoutExercise
from .serializers import WorkoutSerializer, WorkoutExerciseSerializer

class WorkoutApiView(APIView):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    # permission_classes = [permissions.IsAuthenticated]  # Optional for authentication

    def get(self, request):
        workout_id = request.query_params.get('id')  # Get the 'id' query parameter

        if workout_id:
            try:
                workout = Workout.objects.get(pk=workout_id)
                serializer = WorkoutSerializer(workout)
                return Response([serializer.data], status=status.HTTP_200_OK)
            except Workout.DoesNotExist:
                return Response({'error': 'Workout not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            workouts = Workout.objects.all()
            serializer = WorkoutSerializer(workouts, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
    
    def post(self, request, *args, **kwargs):
        data = request.data

        serializer = WorkoutSerializer(data=data)
        if serializer.is_valid():
            # Save the serializer instance to get the created object
            instance = serializer.save()

            # Get the ID of the created object
            created_id = instance.id

            # Include the ID in the response data
            response_data = serializer.data
            response_data['id'] = created_id
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        workout_id = request.query_params.get('id')
        data = request.data

        try:
            workout = Workout.objects.get(pk=workout_id)
        except Workout.DoesNotExist:
            return Response({'error': 'Workout not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = WorkoutSerializer(workout, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        workout_id = request.query_params.get('id')

        try:
            workout = Workout.objects.get(pk=workout_id)
        except Workout.DoesNotExist:
            return Response({'error': 'Workout not found'}, status=status.HTTP_404_NOT_FOUND)

        workout.delete()
        return Response({'message': 'Workout deleted'}, status=status.HTTP_204_NO_CONTENT)
    
class WorkoutExerciseApiView(APIView):
    def get(self, request):
        workout_exercise_id = request.query_params.get('id')
        workout_id = request.query_params.get('workout_id')

        if workout_exercise_id:
            try:
                workout_exercise = WorkoutExercise.objects.get(pk=workout_exercise_id)
                serializer = WorkoutExerciseSerializer(workout_exercise)
                return Response([serializer.data], status=status.HTTP_200_OK)
            except WorkoutExercise.DoesNotExist:
                return Response({'error': 'WorkoutExercise not found'}, status=status.HTTP_404_NOT_FOUND)
        elif workout_id:
            # Retrieve all workout exercises for a specific workout
            workout_exercises = WorkoutExercise.objects.filter(workout_id=workout_id)
        else:
            # Retrieve all workout exercises (default)
            workout_exercises = WorkoutExercise.objects.all()

        serializer = WorkoutExerciseSerializer(workout_exercises, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        data = request.data

        serializer = WorkoutExerciseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        workout_exercise_id = request.query_params.get('id')
        data = request.data

        try:
            workout_exercise = WorkoutExercise.objects.get(pk=workout_exercise_id)
        except WorkoutExercise.DoesNotExist:
            return Response({'error': 'WorkoutExercise not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = WorkoutExerciseSerializer(workout_exercise, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        workout_exercise_id = request.query_params.get('id')

        try:
            workout_exercise = WorkoutExercise.objects.get(pk=workout_exercise_id)
        except WorkoutExercise.DoesNotExist:
            return Response({'error': 'WorkoutExercise not found'}, status=status.HTTP_404_NOT_FOUND)

        workout_exercise.delete()
        return Response({'message': 'WorkoutExercise deleted'}, status=status.HTTP_204_NO_CONTENT)
