from django.contrib import admin
from django.urls import path
from apiRest import views

urlpatterns = [
    path('api/edificios', views.edificios),
]
