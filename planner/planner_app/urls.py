from django.urls import path
from .views import index_view, WorkoutListView, CreateWorkoutView

urlpatterns = [
    path('', index_view, name='index'),
    path('workout_list/', WorkoutListView.as_view(), name='workout_list'),
    path('create_workout/', CreateWorkoutView.as_view(), name='create_workout'),
    
    
]

