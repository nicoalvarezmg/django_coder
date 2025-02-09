from home.views import home, saludo
from django.urls import path


urlpatterns = [
    path('prueba-home/', home, name='home'),
    path('saludo/<str:nombre>/<str:apellido>/', saludo, name='saludo')
]