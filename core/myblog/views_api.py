from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse
# Create your views here.



def loadAboutMe(request: HttpRequest, page:str):
    ''' Will be the API point '''
    # print(page)
    if request.method == 'GET':
        # Page.objects.get(name=page)
        # return JsonResponse({'page' : 'Hello Vue!!!!'})
        return JsonResponse({'page' : 'Hello Vue!!!!'})
        # return HttpResponse(render(request, '<h1>Hello Vue!!</h1>', {})) # Will return JSON object in the future.
    # return HttpResponse(render(request, '<h1>Hello  ????   Vue!!</h1>', {})) # Delete later.
    