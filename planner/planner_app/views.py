from django.shortcuts import render, redirect
from django.views import View
from .models import Workout
from .forms import WorkoutForm

class CreateWorkoutView(View):
    def get(self, request):
        form = WorkoutForm()
        return render(request, 'planner_app/create_workout.html', {'form': form})

    def post(self, request):
        form = WorkoutForm(request.POST)
        if form.is_valid():
            workout = form.save(commit=False)
            workout.save()
            return redirect('workout_list')
        return render(request, 'planner_app/create_workout.html', {'form': form})
    
class WorkoutListView(View):
    def get(self, request):
        workouts = Workout.objects.all()
        return render(request, 'planner_app/workout_list.html', {'workouts': workouts})

def index_view(request):
    return render(request, 'planner_app/index.html')

