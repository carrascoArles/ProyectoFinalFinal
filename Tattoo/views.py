from .models import ImagenTattoos,Tatuador
from django.shortcuts import render, redirect,get_object_or_404
from django.core.mail import send_mail
from .forms import *

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
        asunto = f"[{user}] {request.POST['asunto']}"
        mensaje = request.POST['mensaje']
        destinatario = tatuador.correo
        envio_exitoso = "El correo se ha enviado exitosamente."

        send_mail(asunto, mensaje, 'correo empresa', [destinatario])
    context = {
        'tatuador': tatuador,
        'envio_exitoso': envio_exitoso
    }
    return render(request, 'pedir_cita.html', context)

def Tatuador(request):

    tattooForm = TattooForm()

    return render(request, 'tatuador.html', {'form': tattooForm})

def Imagenes(request):

    sub_Form = ImagenForm()

    return render(request, 'imagen.html', {'form1': sub_Form})

def Usuario(request):

    sub_Form = Usuario()

    return render(request, 'usuario.html', {'form2': sub_Form})