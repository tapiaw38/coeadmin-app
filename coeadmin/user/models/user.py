# Django.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
# utilities
from coeadmin.utils.models import BaseModel

# Create your models here.

class User(BaseModel, AbstractUser):
    """ Modelo de usuario.
    hereda del modelo abstracto AbstractUser
    cambiando la autenticacion de usuario por
    el campo email.
    """
    email = models.EmailField(
        'email addres', 
        unique = True,
        error_messages = {
            'unique': 'Ya existe un usuario con este correo electrónico.',
        }
        )

    phone_regex = RegexValidator(
        regex=r'\d{10,10}$',
        message= "Debes ingresar un número con el siguiente formato: 3837430000. Hasta 10 digitos."
    )

    phone_number = models.CharField(validators=[phone_regex], max_length=10, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name']

    is_admin = models.BooleanField(
        'admin',
        default = True
    )

    is_pollster = models.BooleanField(
        'pollster',
        default = True
    )

    is_verified = models.BooleanField(
        'verified',
        default = True
    )

    def __str__(self):
        """ Retorna el nombre y apellido de usuario. """
        return '{} {}'.format(self.first_name,self.last_name)

    def get_short_name(self):
        """ Retorna el  username. """
        return str(self.username)