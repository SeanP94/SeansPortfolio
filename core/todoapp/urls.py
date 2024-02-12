from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('addTask/', views.addTask),
    path('deleteTask/<str:task>', views.deleteTask, name='deleteTask'),
    path('todolist/', views.addTask)

]