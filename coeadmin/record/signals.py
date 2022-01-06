""" Record signals. """

# Django
from django.db.models.signals import post_save
from django.dispatch import receiver

# Models
from coeadmin.record.models import (
    Positive
)

# Utilities


@receiver(post_save, sender=Positive)
def update_contacts(sender, instance, **kwargs):
    
    instance.con

@receiver(post_save, sender=Positive)
def save_isolation(sender, instance, **kwargs):
    instance.save()
    return instance

