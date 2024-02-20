from django.urls import path
from . import views

urlpatterns = [
    path('helloWorld/', views.helloWorld),
    path('', views.taskList, name="taks-list"),
    path('yourname/<str:name>', views.yourName),
]
