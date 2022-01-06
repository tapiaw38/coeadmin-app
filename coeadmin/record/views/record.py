""" Record views. """

# Django REST Framework.
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Serializers
from coeadmin.record.serializers.record import (
    PositiveModelSerializer,
    ListPositiveSerializer
)

# Models
from coeadmin.record.models.positive import Positive

# Utilities
from coeadmin.record.paginations import StandardResultsSetPagination

class RecordViewSet(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    viewsets.GenericViewSet):
    """ Record view set. """

    queryset = Positive.objects.all()
    serializer_class = PositiveModelSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = StandardResultsSetPagination


    def get_serializer_class(self):
        """ Return the serializer class. """

        if self.action == 'list':
            return ListPositiveSerializer
        return PositiveModelSerializer
        