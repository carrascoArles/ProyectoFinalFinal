from django.urls import path
from . import views


urlpatterns = [
    path ('', views.vista_tatuajes, name = 'vista_tatuajes'),
    path ('pedir_cita/<int:tatuador_dni>',views.pedir_cita,name='pedir_cita'),
    path('formulario/', views.Tatuador, name='mi_f'),
]
