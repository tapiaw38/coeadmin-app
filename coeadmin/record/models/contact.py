""" Contact model. """

# Django
from django.db import models

# Utilities
from coeadmin.utils.models import BaseModel

# Create your models here.


class Contact(BaseModel):
    """
    A contact is the table that 
    maintains the relationship between
    a positive person and close contact.
    """

    person = models.ForeignKey(
        'record.Person',
        related_name='person_contact',
        on_delete=models.CASCADE
    )

    positive = models.ForeignKey(
        'record.Positive',
        on_delete=models.CASCADE
    )

    contact_date = models.DateField(null=True)
    contact_type = models.CharField(max_length=100)
    insolation_days = models.IntegerField(default=0)

    is_active = models.BooleanField(
        'active_contact',
        default=False
    )


    def __str__(self):
        return 'The person {} is in contact with {}'.format(
            self.person,
            self.positive.person
        )