from django.shortcuts import render

from django.http import HttpResponse, HttpRequest
# Create your views here.


def home(request: HttpRequest):
    return HttpResponse(render(request, 'homepage.html', {}))
