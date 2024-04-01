from django import forms

from .models import TaskGroup

class TaskForm(forms.Form):
    name = forms.CharField(label='Task Name', max_length=100)
    due_date = forms.CharField(label='Task Due Date')
    taskgroup = forms.ModelChoiceField(label='Task Group', queryset=TaskGroup.objects.all())