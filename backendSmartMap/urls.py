from django.contrib import admin
from django.urls import path
from apiRest import views

urlpatterns = [
    path('api/edificios', views.edificios),
    path('api/edificios/<str:nombre>/', views.edificio),
    path('api/nodos', views.nodos),
    path('api/nodos/<str:idNodo>/', views.nodo)
]
