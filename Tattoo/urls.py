from django.urls import path
from . import views

urlpatterns = [
    path('formulario/', views.Tatuador, name='mi_f'),

]