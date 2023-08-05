from django.shortcuts import render
from .models import ImagenTattoos,Tatuador

def vista_tatuajes(request):
    tatuadores = Tatuador.objects.all()
    tatuajes = ImagenTattoos.objects.all()
    if  request.user.is_authenticated and request.user.is_staff:
        is_staff = True
    else:
        is_staff = False
    context ={
      'tatuadores': tatuadores,
      'tatuajes': tatuajes,
      'is_staff': is_staff,
    }
    return render(request, 'home.html', context)