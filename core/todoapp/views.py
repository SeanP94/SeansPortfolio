from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from .models import Tasks


# Create your views here.


def home(request: HttpRequest):
    return HttpResponse(render(request, 'todo.html', {"tasks" : Tasks.objects.all()}))


def addTask(request : HttpRequest):
    '''Test to just do a click for htmx-get'''
    if not request.user.is_authenticated:
        return HttpResponse(render(request, 'notify-login.html'))
    newTask = request.POST.get('taskName')
    if newTask != '' and not Tasks.objects.filter(name=newTask):        
        task = Tasks(name=newTask, author=request.user)
        task.save()

    return HttpResponse(render(request, 'todo-list.html', {"tasks" : Tasks.objects.all()}))

def deleteTask(request : HttpRequest, task):
    '''Test to just do a click for htmx-get'''

    if request.method == 'DELETE':
        Tasks.objects.get(name=task).delete()
    return HttpResponse(render(request, 'todo-list.html', {"tasks" : Tasks.objects.all()}))

def loginUser(request):
    
    if request.method == 'GET':
        return HttpResponse(render(request, 'registration/login.html'))
    if request.method == 'POST':
        user = request.POST.get('username')
        passw = request.POST.get('password')
        user = authenticate(request, username=user, password=passw)
        if user is not None:
            
            login(request, user)
            return redirect('homepage')
        else:
            return redirect('login')
    return HttpResponse(render(request, 'registration/login.html'))


def logoutUser(request):
    logout(request)
    return redirect('homepage')
