""" Contact serializers. """

# Django REST Framework
from rest_framework import serializers


# Models
from coeadmin.record.models import Contact, Person, person, positive

# Serializers
from coeadmin.record.serializers.person import PersonModelSerializer


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
            'is_active',
        )
        read_only_fields = (
            'id',
            'person'
        )


class AddContactSerializer(serializers.Serializer):
    """ Add contact serializer. """
    class Meta:
        """ Meta class. """

        fields = (
            'id',
            'person',
            'contact_date',
            'contact_type',
            'insolation_days',
        )


    def create(self, validate_data):
        """ Create the contact. """

        positive = self.context['positive']
        person_id = self.context['request'].data['person']

        person = Person.objects.get(id=person_id)

        contact = Contact.objects.create(
            positive=positive,
            person=person,
            contact_date=self.context['request'].data['contact_date'],
            contact_type=self.context['request'].data['contact_type'],
            insolation_days=self.context['request'].data['insolation_days'],
        )

        return contact