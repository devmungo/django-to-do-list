from django.shortcuts import render, redirect

from django.http import HttpResponse

from . models import Task

from . forms import TaskForm

def index(request):

    form = TaskForm() #this is to create a new task form

    tasks = Task.objects.all() #this is to get all the tasks from the database

    if request.method == 'POST':
        form = TaskForm(request.POST) #this is to create a new task form with the data from the request
        if form.is_valid():
            form.save() #this is to save the form to the database
        return redirect('/')

    context = {'tasks': tasks, 'TaskForm': form} #this is to pass the tasks to the template

    return render(request, 'tasks.html', context)


def updateTask(request, pk):

    task = Task.objects.get(id=pk) #this is to get the task from the database

    form = TaskForm(instance=task) #this is to create a new task form with the data from the request

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task) #this is to create a new task form with the data from the request
        if form.is_valid():
            form.save() #this is to save the form to the database
            return redirect('/')
    
    context = {'TaskForm': form} #this is to pass the tasks to the template

    return render(request, 'update-task.html', context)

def deleteTask(request, pk):

    task = Task.objects.get(id=pk) #this is to get the task from the database

    if request.method == 'POST':
        task.delete() #this is to delete the task from the database
        return redirect('/')

    context = {'task': task} #this is to pass the tasks to the template

    return render(request, 'delete-task.html', context) 
