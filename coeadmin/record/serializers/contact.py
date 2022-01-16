""" Contact serializers. """

# Django REST Framework
from ast import Num
from statistics import mode
from rest_framework import serializers


# Models
from coeadmin.record.models.person import Person
from coeadmin.record.models.contact import Contact

# Serializers
from coeadmin.record.serializers.person import PersonModelSerializer


# Utilities
from datetime import datetime, timedelta

class ContactModelSerializer(serializers.ModelSerializer):
    """ Contact serializer. """

    person = PersonModelSerializer(allow_null=True)

    class Meta:
        """ Meta class. """

        model = Contact
        fields = (
            'id',
            'person',
            'contact_date',
            'contact_type',
            'insolation_days',
            'high_insulation_date',
            'is_active',
        )
        read_only_fields = (
            'id',
            'person'
        )


class AddContactSerializer(serializers.ModelSerializer):
    """ Add contact serializer. """
    class Meta:
        """ Meta class. """
        model = Contact
        fields = (
            'id',
            'person',
            'contact_date',
            'contact_type',
            'insolation_days',
            'high_insulation_date',
            'is_active',
        )


    def create(self, validate_data):
        """ Create the contact. """

        positive = self.context['positive']
        person = validate_data['person']
        days = validate_data['insolation_days']
        contact_date= validate_data['contact_date'],

        contact = Contact.objects.create(
            positive=positive,
            person=person,
            contact_date= validate_data['contact_date'],
            contact_type= validate_data['contact_type'],
            insolation_days=days,
            high_insulation_date=contact_date[0] + timedelta(days=days),
        )

        return contact