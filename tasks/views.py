from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello World")

def task_list(request):
    ctx = {
        "tasks" : [
            'Task 1',
            'Task 2', 
            'Task 3', 
            'Task 4', 
        ]
    }

    return render(request, "task_list.html", ctx)