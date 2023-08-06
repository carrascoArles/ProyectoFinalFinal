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

def vista_tatuadores(request):
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
    return render(request, 'admin.html', context)

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

def crear_tatuador(request):
    if request.method == 'POST':
        tattooForm = TattooForm(request.POST, request.FILES)
        if tattooForm.is_valid():
            tattooForm.save()
            return redirect('http://127.0.0.1:8000/creartatuador/')
    else:
        tattooForm = TattooForm()

    return render(request, 'tatuador.html', {'form': tattooForm})

def Imagenes(request):

    if request.method == 'POST':
        tattooForm = ImagenForm(request.POST, request.FILES)
        if tattooForm.is_valid():
            tattooForm.save()
            return redirect('http://127.0.0.1:8000/imagentatu/')
    else:
        tattooForm = ImagenForm()

    return render(request, 'imagen.html', {'form1': tattooForm})

def crear_usuario(request):

    sub_Form = Usuario()

    return render(request, 'usuario.html', {'form2': sub_Form})

def eliminar_tatuador(request, tatuador_dni):
    tatuadores = get_object_or_404(Tatuador, dni=tatuador_dni)

    if request.method == 'POST':
        tatuadores.delete()
        return redirect('http://127.0.0.1:8000/vistaadmin/')
    context = {
        'tatuadores': tatuadores,
    }
    return render(request, 'confirmacion_eliminacion.html', context)

def administrar_tatuadores(request):
    tatuadores = Tatuador.objects.all()
    context ={
      'tatuadores': tatuadores,
    }
    return render(request, 'admin.html', context)