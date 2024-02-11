from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('addTask/', views.addTask),
    path('deleteTask/', views.deleteTask),
    path('todolist/', views.addTask)

]