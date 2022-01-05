""" Record serializers. """

# Django REST Framework
from datetime import datetime
from rest_framework import serializers


# Models
from coeadmin.record.models import (
    Positive,
    Isolation,
) 


# Serializers


class IsolationSerializer(serializers.ModelSerializer):
    """ Isolation serializer. """

    class Meta:
        """ Meta class. """

        model = Isolation
        fields = (
            'id',
            'isolation_date',
            'days_isolation',
            'high_insulation',
            'high_insulation_date',
        )


class PositiveModelSerializer(serializers.ModelSerializer):
    """ Positive serializer. """

    user = serializers.StringRelatedField()
    isolation = IsolationSerializer(allow_null=True)

    class Meta:
        """ Meta class. """

        model = Positive
        fields = (
            'id',
            'user',
            'person',
            'positivity_date',
            'variant_type',
            'laboratory',
            'contacts_count',
            'isolation',
        )

    def create(self, validate_data):
        """ Create the positive. """

        user =  self.context['request'].user
        profile = user.profile
        profile.polls += 1
        profile.save()

        isolation_data = validate_data.pop('isolation')

        positive = Positive.objects.create(
            user=user,
            profile=profile,
            **validate_data
        )

        # Create the positive isolation.
        
        Isolation.objects.create(
            positivity=positive,
            **isolation_data
        )
        
        return positive

    def update(self, instance, validate_data):
        """ Update the positive. """

        isolation_data = validate_data.pop('isolation')

        isolation = instance.isolation

        # Update the positive

        instance.person = validate_data.get(
            'person', 
            instance.person
        )
        instance.positivity_date = validate_data.get(
            'positivity_date', 
            instance.positivity_date
        )
        instance.variant_type = validate_data.get(
            'variant_type', 
            instance.variant_type
        )
        instance.laboratory = validate_data.get(
            'laboratory', 
            instance.laboratory
        )

        instance.save()

        # Update the positive isolation.

        isolation.isolation_date = isolation_data.get(
            'isolation_date',
            isolation.isolation_date
        )
        isolation.days_isolation = isolation_data.get(
            'days_isolation',
            isolation.days_isolation
        )
        isolation.high_insulation = isolation_data.get(
            'high_insulation',
            isolation.high_insulation
        )

        if isolation.high_insulation == True:
            isolation.high_insulation_date = datetime.today().strftime('%Y-%m-%d')
            
        elif isolation.high_insulation == False:
            isolation.high_insulation_date = None
            
        isolation.save()

        return instance