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
    envio_exitoso = "" 
    if request.method == 'POST':
        user = request.user
        asunto = request.POST['asunto']
        mensaje = request.POST['mensaje']
        destinatario = tatuador.correo
        envio_exitoso = "El correo se ha enviado exitosamente."

        send_mail(asunto, mensaje, 'correo empresa', [destinatario])
    context = {
        'tatuador': tatuador,
        'envio_exitoso': envio_exitoso
    }
    return render(request, 'pedir_cita.html', context)