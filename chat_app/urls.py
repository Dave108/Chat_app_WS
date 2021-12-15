from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('<str:room_name>/', views.room, name='room'),

]
