from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response

from .models import Exercise
from .serializers import ExerciseSerializer

class ExerciseApiView(APIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    # permission_classes = [permissions.IsAuthenticated]  # Optional for authentication

    def get(self, request):
        exercise_id = request.query_params.get('id')  # Get the 'id' query parameter

        if exercise_id:
            try:
                exercise = Exercise.objects.get(pk=exercise_id)
                serializer = ExerciseSerializer(exercise)
                # Wrap the serialized data in a list
                return Response([serializer.data], status=status.HTTP_200_OK)
            except Exercise.DoesNotExist:
                return Response({'error': 'Exercise not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            exercises = Exercise.objects.all()
            serializer = ExerciseSerializer(exercises, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    
    # def post(self, request, *args, **kwargs):
    #     data = request.data

    #     serializer = ExerciseSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # def put(self, request):
    #     exercise_id = request.query_params.get('id')
    #     data = request.data

    #     try:
    #         exercise = Exercise.objects.get(pk=exercise_id)
    #     except Exercise.DoesNotExist:
    #         return Response({'error': 'Exercise not found'}, status=status.HTTP_404_NOT_FOUND)

    #     serializer = ExerciseSerializer(exercise, data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # def delete(self, request):
    #     exercise_id = request.query_params.get('id')

    #     try:
    #         exercise = Exercise.objects.get(pk=exercise_id)
    #     except Exercise.DoesNotExist:
    #         return Response({'error': 'Exercise not found'}, status=status.HTTP_404_NOT_FOUND)
        
    #     exercise.delete()
    #     return Response({'message': 'Exercise deleted'}, status=status.HTTP_204_NO_CONTENT)
