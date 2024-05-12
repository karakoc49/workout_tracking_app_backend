from django.urls import path
from .views import ExerciseApiView

urlpatterns = [
    path('exercise/', ExerciseApiView.as_view())
]