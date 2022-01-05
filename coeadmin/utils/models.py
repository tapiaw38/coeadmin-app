from django.db import models

# Create your models here.

class BaseModel(models.Model):
    """ Modelo base produccion.
    Esta es una clase abstracta que los demas modelos heredaran.
    """

    created = models.DateTimeField('create at',auto_now_add=True)
    modified = models.DateTimeField('modified at', auto_now=True)

    class Meta:
        """ Opciones Meta """
        abstract = True

        get_latest_by = 'created'
        ordering = ['-created', '-modified']

