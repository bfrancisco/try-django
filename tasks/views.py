from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Task


def index(request):
    return HttpResponse("Hello World")


def task_list(request):
    tasks = Task.objects.all()
    ctx = {
        "tasks" : tasks
    }
    return render(request, "task_list.html", ctx)


def task_detail(request, pk):
    task = Task.objects.get(pk=pk)
    ctx = { "task" : task }
    return render(request, 'task_detail.html', ctx)

class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'

class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'task_detail.html'
