from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from Tattoo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('', include('Tattoo.urls')),
    path('tatuador/',views.crear_tatuador, name='assag'),
    path('imagentatu/',views.Imagenes, name='assag'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
