from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def home(request):
    # template = loader.get_template('todo.html')
    # print(template)
    context = {
        "tasks" : [f"Task: {x}" for x in range(1,16)]
    }
    return HttpResponse(render(request, 'todo.html', context=context))