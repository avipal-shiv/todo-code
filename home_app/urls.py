from django.contrib import admin
from django.urls import include, path

from . import views

app_name='home_app'

urlpatterns = [
    path('', views.index, name='index'),
    
]
