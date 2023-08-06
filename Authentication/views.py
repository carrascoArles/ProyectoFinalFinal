import requests
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import LoginForm, RegisterForm
from .models import UserData

def homeView(request):
    return render(request, 'home.html', {'user': request.user})

def loginView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            dni = form.cleaned_data.get('dni')
            password = form.cleaned_data.get('contraseña')
            user = UserData.objects.authenticate_user(dni=dni, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def registerView(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            dni = form.cleaned_data['dni']
            nombres = form.cleaned_data['nombres']
            apellidos = form.cleaned_data['apellidos']
            telefono = form.cleaned_data['telefono']
            email = form.cleaned_data['email']
            password = form.cleaned_data['contraseña'] 

            if validate_dni(dni, nombres, apellidos):
                UserData.objects.create(dni=dni, nombres=nombres, apellidos=apellidos, telefono=telefono, email=email, rol='Cliente', password=password)
                return redirect('home')
            else:
                alert_message = "Los datos ingresados no coinciden con el DNI. Verifícalos e intenta nuevamente."
                return render(request, 'register.html', {'form': form, 'alert_message': alert_message})
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def validate_dni(dni, nombres, apellidos):
    url = f'https://dniruc.apisperu.com/api/v1/dni/{dni}?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6InJleXNlci56YXAuMTQ1QGdtYWlsLmNvbSJ9.e_VtxCOl5DDGy4tU32LZ8UwOCbidFwnEV24rn470pTw'
    response = requests.get(url)
    data = response.json()
    if data.get('success', False):
        api_nombres = data.get("nombres", "").upper().replace(" ", "")
        api_apellidos = (data.get("apellidoPaterno","") + data.get("apellidoMaterno","")).upper().replace(" ", "")
        return api_nombres == nombres.upper().replace(" ", "") and api_apellidos == (apellidos).upper().replace(" ", "")
    return False
