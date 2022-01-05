""" Contact serializers. """

# Django REST Framework
from rest_framework import serializers


# Models
from coeadmin.record.models import (
    Contact,
) 


# Serializers


class ContactSerializer(serializers.ModelSerializer):
    """ Contact serializer. """

    class Meta:
        """ Meta class. """

        model = Contact
        fields = (
            'id',
            'person',
            'contact_date',
            'contact_type',
            'insolation_days',
            'is_active',
        )
