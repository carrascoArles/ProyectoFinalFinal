from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from Tattoo import views
from Authentication.views import loginView, registerView
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import redirect

def is_admin(user):
    return user.is_authenticated and user.rol == 'Administrador'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', loginView, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page=views.vista_tatuajes), name='logout'),
    path('register/', registerView, name='register'),
    path('tatuador/', views.Tatuador, name='assag'),
    path ('', include('Tattoo.urls')),
    path('creartatuador/', views.crear_tatuador, name='creartatuador'),
    path('imagentatu/', views.Imagenes, name='imagentatu'),
    path('vistaadmin/', user_passes_test(is_admin, login_url='/')(views.administrar_tatuadores), name='vistaadmin'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
