from django.shortcuts import render
from todoapp.models import Task
from django.http import HttpResponseRedirect
from todoapp.forms import TaskCreate

def listTasks(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks': tasks}) 

def createTask(request):
    task = Task(title=request.POST['title'])
    task.save()
    return HttpResponseRedirect('/todo/')

def deleteTask(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return HttpResponseRedirect('/todo/')

def editTask(request, pk):
    task = Task.objects.get(pk=pk)
    taskForm = TaskCreate(instance=task, data=request.POST)
    if taskForm.is_valid():
        taskForm.save()
    return HttpResponseRedirect('/todo/')

def editPage(request, pk):
    task = Task.objects.get(pk=pk)
    # taskForm = TaskCreate(instance=task, data=request.POST)
    # if taskForm.is_valid():
    #     taskForm.save()

    return render(request, 'editPage.html', {'task': task}) 