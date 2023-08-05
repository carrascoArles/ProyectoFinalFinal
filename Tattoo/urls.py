from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path ('', views.vista_tatuajes, name = 'vista_tatuajes'),
    path ('pedir_cita/<int:tatuador_dni>',views.pedir_cita,name='pedir_cita'),
]
