from django.shortcuts import render, redirect
from .forms import *

def Tatuador(request):

    tattooForm = TattooForm()

    return render(request, 'tatuador.html', {'form': tattooForm})

def Imagenes(request):

    sub_Form = ImagenForm()

    return render(request, 'imagen.html', {'form1': sub_Form})

def Usuario(request):

    sub_Form = Usuario()

    return render(request, 'usuario.html', {'form2': sub_Form})