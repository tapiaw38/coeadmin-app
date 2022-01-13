# Django.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
# utilities
from coeadmin.utils.models import BaseModel

# Create your models here.

class User(BaseModel, AbstractUser):
    """ 
    User model.
    inherits from AbstractUser abstract model
    changing user authentication to
    the email field.
    """

    email = models.EmailField(
        'email addres', 
        unique = True,
        error_messages = {
            'unique': 'There is already a user with this email.',
        }
    )

    phone_regex = RegexValidator(
        regex=r'\d{10,10}$',
        message= "You must enter a number with the following format: 3837430000. Up to 10 digits."
    )

    phone_number = models.CharField(
        validators=[phone_regex], 
        max_length=10, 
        blank=True, 
        null=True
    )

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
        """ Return the first name and lastname. """
        
        return '{} {}'.format(self.first_name,self.last_name)

    def get_short_name(self):
        """ Return the username. """

        return str(self.username)