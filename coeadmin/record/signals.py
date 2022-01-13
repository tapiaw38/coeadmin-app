""" Record signals. """

# Django
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Models
from coeadmin.record.models.positive import Positive
from coeadmin.record.models.isolation import Isolation

# Utilities
from datetime import datetime, timedelta


@receiver(pre_save, sender=Positive)
def update_isolation(sender, instance, **kwargs):

    """ Update the isolation date. """


    if instance.isolation.isolation_date:
        instance.isolation.high_insulation_date = instance.isolation.isolation_date + \
                                                    timedelta(days=instance.isolation.days_isolation)
        instance.isolation.save()
    

