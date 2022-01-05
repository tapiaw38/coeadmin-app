""" Location model. """

# Django.
from django.db import models

# Utilities.
from coeadmin.utils.models import BaseModel

# Create your models here.


class Location(BaseModel):
    """ Model of the person's location. """

    person = models.OneToOneField(
        'record.Person', 
        related_name='location',
        on_delete=models.CASCADE
    )

    district = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    address = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)

    def __str__(self):
        """ The person's location. """

        return 'The person {} is located in {}'.format(
            self.person,
            self.district
        )