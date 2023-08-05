from django.shortcuts import render, redirect
from .forms import *

def Tatuador(request):
    if request.method == 'POST':
        tattooForm = TattooForm(request.POST, request.FILES)
        if tattooForm.is_valid():
            tattooForm.save()
            return redirect('http://127.0.0.1:8000/imagentatu/')
    else:
        tattooForm = TattooForm()

    return render(request, 'tatuador.html', {'form': tattooForm})

def Imagenes(request):

    if request.method == 'POST':
        tattooForm = ImagenForm(request.POST, request.FILES)
        if tattooForm.is_valid():
            tattooForm.save()
            return redirect('http://127.0.0.1:8000/tatuador/')
    else:
        tattooForm = ImagenForm()

    return render(request, 'tatuador.html', {'form1': tattooForm})

def Usuario(request):

    sub_Form = Usuario()

    return render(request, 'usuario.html', {'form2': sub_Form})