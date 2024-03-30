from django.shortcuts import render

from django.http import HttpResponse, HttpRequest, JsonResponse
# Create your views here.


def home(request: HttpRequest):
    return HttpResponse(render(request, 'homepage.html', {}))


def resume(request: HttpRequest):
    return HttpResponse(render(request, 'resume.html', {}))



def My404_view(request: HttpRequest, exception):
    return HttpResponse(render(request, '404.html', {}))


