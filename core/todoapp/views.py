from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

context = {
        "tasks" : [f"Task: {x}" for x in range(1,16)]
    }

def home(request):
    # template = loader.get_template('todo.html')
    # print(template)
    
    return HttpResponse(render(request, 'todo.html', context=context))


def clickTest(request):
    '''Test to just do a click for htmx-get'''
    
    print("Test Successful!")
    return HttpResponse(render(request, 'todo-list.html', context=context))