from django.shortcuts import render
from django.http import HttpResponse
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

