from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('todos/', views.todos, name='todos'),
    path('toggle-complete/<int:id>/', views.toggle_complete, name='toggle_complete'),
    path('delete-task/<int:id>/', views.delete_task, name='delete_task'),
    path('add-task/', views.add_task, name='add_task'),
]

from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title