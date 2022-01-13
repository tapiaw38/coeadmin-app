""" Person model. """

# Django.
from django.db import models
from django.core.validators import RegexValidator

# Utilities.
from coeadmin.utils.models import BaseModel

# Create your models here.

class Person(BaseModel):
    """ Person model. """

    first_name = models.CharField(max_length=50)
    
    last_name = models.CharField(max_length=50)

    document_regex = RegexValidator(
        regex=r'\d{8,8}$',
        message="You must enter a DNI number without points."
    )
    document = models.CharField(
        validators=[document_regex], 
        max_length=8,
        unique=True,
    )
    
    date_birth = models.DateField(
        null=True,
        blank=True,
    )
    
    gender = models.CharField(max_length=10)

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

    def __str__(self):
        """ Return the first name and lastname. """
        
        return '{} {}'.format(self.first_name,self.last_name)