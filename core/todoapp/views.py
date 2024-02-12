from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.template import loader
from django.contrib.auth import authenticate, login, logout


# Create your views here.

context = {
        "tasks" : []
    }

def home(request: HttpRequest):
    # template = loader.get_template('todo.html')
    # print(template)
    print(request.user.is_authenticated)
    return HttpResponse(render(request, 'todo.html', context=context))


def addTask(request : HttpRequest):
    '''Test to just do a click for htmx-get'''
    if not request.user.is_authenticated:
        return HttpResponse(render(request, 'notify-login.html'))
    newTask = request.POST.get('taskName')
    if newTask != '' and newTask not in context['tasks']: context['tasks'].append(newTask)
    return HttpResponse(render(request, 'todo-list.html', context=context))

def deleteTask(request : HttpRequest, task):
    '''Test to just do a click for htmx-get'''
    if request.method == 'DELETE':
        context['tasks'].remove(task)
    return HttpResponse(render(request, 'todo-list.html', context=context))

def loginUser(request):
    print('helloooo')
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
