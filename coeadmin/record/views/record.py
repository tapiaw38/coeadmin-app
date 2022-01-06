""" Record views. """

# Django REST Framework.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Serializers
from coeadmin.record.serializers.record import PositiveModelSerializer

# Models
from coeadmin.record.models.positive import Positive

# Utilities
from coeadmin.record.paginations import StandardResultsSetPagination

class RecordViewSet(viewsets.ModelViewSet):
    """ Record view set. """

    queryset = Positive.objects.all()
    serializer_class = PositiveModelSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = StandardResultsSetPagination
