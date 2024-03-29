from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='Homepage'),
    path('resume/', views.resume, name='ResumePage'),
    path('gets/loadAboutMe/<str:page>', views.loadAboutMe, name='loadAboutMe'),
    
    path('404/', views.My404_view)
]


handler404 = 'myblog.views.My404_view'