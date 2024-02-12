from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('addTask/', views.addTask),
    path('deleteTask/<str:task>', views.deleteTask, name='deleteTask'),
    path('login/', include('django.contrib.auth.urls')),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout')
]