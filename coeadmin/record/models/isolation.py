""" Isolation model. """

# Django.
from django.db import models

# Utilities.
from coeadmin.utils.models import BaseModel

# Create your models here.


class Isolation(BaseModel):
    """ Isolation model. """

    positivity = models.OneToOneField(
        'record.Positive',
        related_name='isolation',
        on_delete=models.CASCADE
    )
    
    isolation_date = models.DateField(blank=True, null=True)
    days_isolation = models.IntegerField(default=0)

    high_insulation = models.BooleanField(default=False)
    high_insulation_date = models.DateField(blank=True, null=True)

    def __str__(self):
        
        return 'The person {} is isolated for {} days'.format(
                self.positivity.person, 
                self.days_isolation
            )