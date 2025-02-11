from home.views import home, saludo, crear_auto, listado_de_autos
from django.urls import path


urlpatterns = [
    path('prueba-home/', home, name='home'),
    path('saludo/<str:nombre>/<str:apellido>/', saludo, name='saludo'),
    path('crear-auto/', crear_auto, name='crear_auto'),
    path("listado-de-autos/", listado_de_autos, name="listado_de_autos")
]