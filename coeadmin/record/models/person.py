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
    document = models.CharField(validators=[document_regex], max_length=8)
    
    date_birth = models.DateField()
    gender = models.CharField(max_length=10)

    def __str__(self):
        """ Return the first name and lastname. """
        
        return '{} {}'.format(self.first_name,self.last_name)