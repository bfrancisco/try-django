from datetime import datetime

from django.db import models
from django.urls import reverse


class TaskGroup(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=100)
    due_date = models.DateTimeField(null=False)
    taskgroup = models.ForeignKey('TaskGroup', 
        on_delete=models.CASCADE, 
        default=1, 
        related_name='tasks'
    )
    task_image = models.ImageField(upload_to="images/", null=True)

    def __str__(self):
        return f'{self.name} due on {self.due_date}'

    def get_absolute_url(self):
        return reverse('tasks:task-detail', args=[str(self.pk)])

    @property
    def is_due(self):
        return datetime.now() >= self.due_date

    class Meta:
        ordering = ['due_date']
        unique_together = [
            ['due_date', 'name'], 
        ]
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks' 
        
        
