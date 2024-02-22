from django.urls import path

from .views import index, task_list, task_detail

urlpatterns = [
    path('', index, name="index"),
    path('list', task_list, name="list"),
    path('<int:pk>/detail', task_detail, name='task-detail'),
]

app_name = "tasks"