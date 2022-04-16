from django.urls import path
from todoapp import views

urlpatterns = [
    path('todo/',views.listTasks),
    path('create/',views.createTask),
    path('delete/<int:pk>/',views.deleteTask),
    path('edit/<int:pk>/',views.editTask),
    path('editPage/<int:pk>/',views.editPage),
]