from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.template import loader
# Create your views here.

context = {
        "tasks" : []
    }

def home(request: HttpRequest):
    # template = loader.get_template('todo.html')
    # print(template)
    
    return HttpResponse(render(request, 'todo.html', context=context))


def addTask(request : HttpRequest):
    '''Test to just do a click for htmx-get'''
    newTask = request.POST.get('taskName')
    if newTask != '' and newTask not in context['tasks']: context['tasks'].append(newTask)
    return HttpResponse(render(request, 'todo-list.html', context=context))

def deleteTask(request : HttpRequest, task):
    '''Test to just do a click for htmx-get'''
    if request.method == 'DELETE':
        print(task)
        context['tasks'].remove(task)
        
        print(request)
    return HttpResponse(render(request, 'todo-list.html', context=context))


def todoList(request : HttpRequest):
    return HttpResponse(render(request,'todo-list.html', context=context))