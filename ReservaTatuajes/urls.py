from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from Tattoo import views
from Authentication.views import homeView, loginView, registerView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeView, name='home'),
    path('login/', loginView, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', registerView, name='register'),
    path('tatuador/',views.Tatuador, name='assag'),
    path ('', include('Tattoo.urls')),
    path('tatuador/',views.crear_tatuador, name='assag'),
    path('imagentatu/',views.Imagenes, name='assag'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
