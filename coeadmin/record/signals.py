""" Record signals. """

# Django
from django.db.models.signals import post_save
from django.dispatch import receiver

# Models
from coeadmin.record.models import (
    Positive
)

# Utilities
from datetime import datetime



@receiver(post_save, sender=Positive)
def update_isolation(sender, instance, **kwargs):
    
    if instance.isolation.high_insulation == True:
        instance.isolation.high_insulation_date = datetime.today().strftime('%Y-%m-%d')
    
    elif instance.isolation.high_insulation == False:
        instance.isolation.high_insulation_date = None

@receiver(post_save, sender=Positive)
def save_isolation(sender, instance, **kwargs):
    instance.isolation.save()
    
    return instance.isolation

