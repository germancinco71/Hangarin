from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from task_manager.models import Task
from task_manager.forms import TaskForm
from django.urls import reverse_lazy


class HomePageView(ListView):
    model = Task
    context_object_name = 'home'
    
class TaskList(ListView):
    model = Task
    context_object_name = 'task'
    template_name = 'task_list.html'
    paginate_by = 5
    
class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('task-list')