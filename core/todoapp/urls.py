from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('addTask/', views.addTask),
    path('deleteTask/<str:task>', views.deleteTask, name='deleteTask'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout')
]