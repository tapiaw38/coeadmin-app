""" Person serializers. """

# Django REST Framework
from rest_framework import serializers


# Models
from coeadmin.record.models import (
    Person,
    Location,
) 


# Serializers


class LocationSerializer(serializers.ModelSerializer):
    """ Location serializer. """

    class Meta:
        """ Meta class. """

        model = Location
        fields = (
            'id',
            'district',
            'address',
            'latitude',
            'longitude',
        )


class PersonModelSerializer(serializers.ModelSerializer):
    """ Person serializer. """

    location=LocationSerializer(allow_null=True)

    class Meta:
        """ Meta class. """

        model = Person
        fields = (
            'id',
            'first_name',
            'last_name',
            'document',
            'date_birth',
            'gender',
            'location'
        )
    
    def create(self, validate_data):
        """ Create relation of the location person. """
        
        location_data = validate_data.pop('location')

        person = Person.objects.create(**validate_data)
        
        # Create the person location.

        Location.objects.create(
            person=person,
            **location_data
        )

        return person


    def update(self, instance, validate_data):
        """ Update the person. """

        location_data = validate_data.pop('location')

        location = instance.location

        # Update the person.

        instance.first_name = validate_data.get(
            'first_name',
            instance.first_name
        )
        instance.last_name = validate_data.get(
            'last_name',
            instance.last_name
        )
        instance.document = validate_data.get(
            'document',
            instance.document
        )
        instance.date_birth = validate_data.get(
            'date_birth',
            instance.date_birth
        )
        instance.gender = validate_data.get(
            'gender',
            instance.gender
        )
        instance.save()

        # Update the person location.

        location.district = location_data.get(
            'district',
            location.district
        ) 
        location.address = location_data.get(
            'address',
            location.address
        )
        location.latitude = location_data.get(
            'latitude',
            location.latitude
        )
        location.longitude = location_data.get(
            'longitude',
            location.longitude
        )
        location.save()

        return instance



