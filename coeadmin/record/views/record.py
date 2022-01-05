""" Record views. """

# Django REST Framework.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Serializers
from coeadmin.record.serializers.record import PositiveModelSerializer
from coeadmin.record.serializers.person import PersonModelSerializer

# Models
from coeadmin.record.models.person import Person
from coeadmin.record.models.positive import Positive

# Utilities
from coeadmin.record.paginations import StandardResultsSetPagination

class RecordViewSet(viewsets.ModelViewSet):
    """ Record view set. """

    queryset = Positive.objects.all()
    serializer_class = PositiveModelSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = StandardResultsSetPagination


class PersonViewSet(viewsets.ModelViewSet):
    """ Person view set. """

    queryset = Person.objects.all()
    serializer_class = PersonModelSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = StandardResultsSetPagination