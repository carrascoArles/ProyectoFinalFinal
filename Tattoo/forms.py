from django import forms
from .models import *

class TattooForm(forms.ModelForm):
    class Meta:
        model = Tatuador
        fields = '__all__'

class ImagenForm(forms.ModelForm):
    class Meta:
        model = ImagenTattoos
        fields = '__all__'

class Usuario(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'