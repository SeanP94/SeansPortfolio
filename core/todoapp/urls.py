from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('testClick/', views.clickTest),
    path('todolist/', views.clickTest)

]