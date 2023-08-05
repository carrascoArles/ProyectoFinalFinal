from django import forms
from django.core.validators import MaxLengthValidator


class BaseForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs.setdefault('autocomplete', 'off')


class LoginForm(BaseForm):
    dni = forms.CharField(label="DNI", max_length=8, widget=forms.TextInput(attrs={
        'placeholder': 'Ingresa tu DNI',
        'data-lpignore': 'true',
    }))

    contraseña = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={
        'placeholder': 'Introduce tu contraseña',
        'data-lpignore': 'true',
    }))


class RegisterForm(BaseForm):
    dni = forms.CharField(label="DNI", max_length=8, widget=forms.TextInput(attrs={
        'placeholder': 'Ingresa tu DNI',
        'data-lpignore': 'true',
    }))

    
    nombres = forms.CharField(label="Nombres", max_length=100, widget=forms.TextInput(attrs={
        'placeholder': 'Ingresa tus nombres',
        'required': True,
    }))
    
    apellidos = forms.CharField(label="Apellidos", max_length=100, widget=forms.TextInput(attrs={
        'placeholder': 'Ingresa tus apellidos',
        'required': True,
    }))

    telefono = forms.CharField(label="Teléfono", max_length=9, widget=forms.TextInput(attrs={
        'placeholder': 'Ingresa tu teléfono',
        'required': True,
    }))

    email = forms.EmailField(label="Correo Electrónico", widget=forms.TextInput(attrs={
        'placeholder': 'Ingresa tu correo electrónico',
        'required': True,
    }))

    contraseña = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={
        'placeholder': 'Crea tu contraseña',
        'required': True,
    }))
