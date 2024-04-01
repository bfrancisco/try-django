from django.contrib import admin

from .models import TaskGroup, Task


class TaskInline(admin.TabularInline):
    model = Task

class TaskGroupAdmin(admin.ModelAdmin):
    model = TaskGroup
    inlines = [TaskInline,]

class TaskAdmin(admin.ModelAdmin):
    model = Task
    list_display = ['name', 'due_date',]
    search_fields = ['name',]
    list_filter = ['due_date',]

    fieldsets = [
        ('Details', {
            'fields' : [
                ('name', 'due_date'), 'taskgroup', 'task_image',
            ]    
        })
    ]


admin.site.register(TaskGroup, TaskGroupAdmin)
admin.site.register(Task, TaskAdmin)