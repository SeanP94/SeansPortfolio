from django.shortcuts import render

from django.http import HttpResponse, HttpRequest, JsonResponse
# Create your views here.


def home(request: HttpRequest):
    return HttpResponse(render(request, 'homepage.html', {}))


def resume(request: HttpRequest):
    return HttpResponse(render(request, 'resume.html', {}))



def My404_view(request: HttpRequest, exception):
    return HttpResponse(render(request, '404.html', {}))


### API Points ###

def loadAboutMe(request: HttpRequest):
    ''' Will be the API point '''
    # print(page)
    if request.method == 'GET':
        # Page.objects.get(name=page)
        return JsonResponse({'page' : 'Hello Vue!!!!'})
        # return HttpResponse(render(request, '<h1>Hello Vue!!</h1>', {})) # Will return JSON object in the future.
    # return HttpResponse(render(request, '<h1>Hello  ????   Vue!!</h1>', {})) # Delete later.
    