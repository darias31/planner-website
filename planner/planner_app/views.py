from django.shortcuts import render, redirect
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie

from .models import Workout
from .forms import WorkoutForm

class WorkoutListView(View):
    def get(self, request):
        workouts = Workout.objects.all()
        context = {}
        context['workouts'] = workouts
        return render(request, 'planner_app/workout_list.html', context)
    
class CreateWorkoutView(View):
    def get(self, request):
        form = WorkoutForm()
        context = {}
        context["form"] = form
        return render(request, 'planner_app/create_workout.html', context)

def index_view(request):
    return render(request, 'planner_app/index.html')