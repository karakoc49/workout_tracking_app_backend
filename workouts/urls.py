from django.urls import path
from .views import WorkoutApiView, WorkoutExerciseApiView

urlpatterns = [
    path('workout/', WorkoutApiView.as_view()),
    path('workout-exercise/', WorkoutExerciseApiView.as_view()),
]