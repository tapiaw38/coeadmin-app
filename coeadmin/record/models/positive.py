""" Positive model. """

# Django.
from django.db import models

# Utilities.
from coeadmin.utils.models import BaseModel

# Create your models here.


class Positive(BaseModel):
    """ 
    Positive model.
    Covid positive people 
    registration model
    """

    user = models.ForeignKey(
        'user.User', 
        on_delete=models.CASCADE
    )
    profile = models.ForeignKey(
        'user.Profile', 
        on_delete=models.CASCADE
    )

    person = models.ForeignKey(
        'record.Person',
        related_name='positive',
        on_delete=models.CASCADE
    )

    positivity_date = models.DateField()
    variant_type = models.CharField(max_length=100)
    laboratory = models.CharField(max_length=100)

    contacts = models.ManyToManyField(
        'record.Person', 
        related_name='contacts',
        through='record.Contact',
        through_fields=('positive', 'person'),
    )

    @property
    def contacts_count(self):
        """ Return the number of contacts. """

        return self.contacts.all().count()

    def __str__(self):
        """ the positive person with covid returns. """

        return 'The person id: {}, {} is positive'.format(self.id,self.person)