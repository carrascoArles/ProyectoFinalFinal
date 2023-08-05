from django.shortcuts import render
from .models import ImagenTattoos,Tatuador
from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail

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
def pedir_cita(request, tatuador_dni):
    tatuador = get_object_or_404(Tatuador, dni=tatuador_dni)

    context = {
        'tatuador': tatuador,
    }
    return render(request, 'pedir_cita.html', context)