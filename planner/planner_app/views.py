from django.shortcuts import render, redirect
from django.views import View

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.urls import reverse

from .models import Workout, ExerciseWithInfo
from .forms import WorkoutForm, ExerciseWithInfoForm, ExerciseWithInfoFormSet


@method_decorator(ensure_csrf_cookie, name="dispatch")
class WorkoutListView(View):
    def get(self, request):
        workouts = Workout.objects.all()
        context = {}
        context["workouts"] = workouts
        return render(request, "planner_app/workout_list.html", context)


"""class CreateWorkoutView(CreateView):
    model = Workout
    form_class = WorkoutForm
    template_name = "planner_app/create_workout.html"

    def form_valid(self, form):
        workout = form.save()
        return redirect("add_exercise", workout_id=workout.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["workout"] = self.object
        return context"""


class CreateWorkoutView(CreateView):
    model = Workout
    form_class = WorkoutForm
    template_name = 'planner_app/create_workout.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['exercise_formset'] = ExerciseWithInfoFormSet(self.request.POST, instance=self.object)
        else:
            context['exercise_formset'] = ExerciseWithInfoFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        exercise_formset = context['exercise_formset']
        if exercise_formset.is_valid():
            self.object = form.save()
            exercise_formset.instance = self.object
            exercise_formset.save()
            return redirect('workout_list')
        else:
            return self.render_to_response(self.get_context_data(form=form))

def index_view(request):
    return render(request, "planner_app/index.html")
