from django.urls import path

from .views import index, TaskListView, TaskUpdateView, TaskCreateView

urlpatterns = [
    path('', index, name="index"),
    path('create', TaskCreateView.as_view()),
    path('list', TaskListView.as_view(), name="list"),
    path('<int:pk>/detail', TaskUpdateView.as_view(), name='task-detail'),
]

app_name = "tasks"