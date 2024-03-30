from django.urls import path, include
from . import views, views_api


urlpatterns = [
    path('', views.home, name='Homepage'),
    path('resume/', views.resume, name='ResumePage'),
    path('gets/loadAboutMe/<str:page>', views_api.loadAboutMe, name='loadAboutMe'),

    path('404/', views.My404_view)
]


handler404 = 'myblog.views.My404_view'