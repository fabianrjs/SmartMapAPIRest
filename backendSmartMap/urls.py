from django.urls import path
from apiRest import views

urlpatterns = [
    path('api/edificios', views.edificios),
    path('api/edificios/<str:nombre>/', views.edificio),
    path('api/nodos', views.nodos),
    path('api/nodos/<str:idNodo>/', views.nodo),
    path('api/usuarios', views.usuarios),
    path('api/usuario/<str:uId>/', views.usuario),
    path('api/ActualizarPosicionUsuario/<str:uId>/<str:nodoAnterior>/<str:nodoActual>', views.actualizarUbicacion),
    path('api/GuardarBusquedaDelUsuario/<str:uId>/<str:busqueda>', views.guardarBusqueda),
    path('api/aforo/<str:id_edificio>', views.aforo),
    path('api/ruta/<str:idNodoInicio>/<str:idNodoFinal>', views.ruta),
]
