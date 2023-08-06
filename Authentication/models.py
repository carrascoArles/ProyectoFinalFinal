from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self, dni, nombres, apellidos, telefono, email, rol, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)

        if not dni:
            raise ValueError('El DNI debe ser proporcionado.')

        user = self.model(
            dni=dni,
            nombres=nombres,
            apellidos=apellidos,
            telefono=telefono,
            email=email,
            rol=rol,
            password=password,
            **extra_fields
        )
        user.save(using=self._db)
        return user


    def create_superuser(self, dni, nombres, apellidos, telefono, email, rol, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser debe tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser debe tener is_superuser=True.')

        return self.create_user(dni, nombres, apellidos, telefono, email, rol, password, **extra_fields)

    def authenticate_user(self, dni=None, password=None):
        try:
            user = self.get(dni=dni)
            if user.password == password:
                return user
            return None
        except self.model.DoesNotExist:
            return None

class UserData(AbstractBaseUser, PermissionsMixin):
    dni = models.CharField(max_length=8, unique=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    telefono = models.CharField(max_length=9, null=True)
    email = models.EmailField(max_length=100, null=True)
    rol = models.CharField(max_length=13, choices=[('Cliente', 'Cliente'), ('Tatuador', 'Tatuador'), ('Administrador', 'Administrador')], default='Cliente')
    password = models.CharField(max_length=100, null=True) 
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    
    objects = UserManager()

    USERNAME_FIELD = 'dni'
    REQUIRED_FIELDS = ['nombres', 'apellidos', 'telefono', 'email', 'rol']

    def __str__(self):
        return self.dni