"""Profile serializer."""

# Django REST Framework
from rest_framework import serializers

# Models
from coeadmin.user.models import Profile



class ProfileModelSerializer(serializers.ModelSerializer):
    """Profile model serializer."""

    class Meta:
        """Meta class."""

        model = Profile
        fields = (
            'picture',
            'polls'
        )
        read_only_fields = (
            'polls',
        )