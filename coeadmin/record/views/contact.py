""" Contact views. """

# Django REST Framework.
from rest_framework import viewsets, mixins, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

# Serializers
from coeadmin.record.serializers.contact import AddContactSerializer, ContactModelSerializer

# Models
from coeadmin.record.models.contact import Contact
from coeadmin.record.models.positive import Positive

# Utilities
from coeadmin.record.paginations import StandardResultsSetPagination


class ContactViewSet(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    viewsets.GenericViewSet):
    """ Contacts view set. """

    serializer_class = ContactModelSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = StandardResultsSetPagination

    def dispatch(self, request, *args, **kwargs):

        id = kwargs.get('id')
        self.positive = get_object_or_404(
            Positive,
            id=id
        )

        return super(ContactViewSet, self).dispatch(request, *args, **kwargs)
    
    def get_queryset(self):
        """ Get queryset. """

        return Contact.objects.filter(
            positive=self.positive
        )

    def create(self, request, *args, **kwargs):
        """ Create contact. """

        serializer = AddContactSerializer(
            data=request.data,
            context={
                'positive': self.positive,
                'request': request
            }
        )
        
        serializer.is_valid(raise_exception=True)
        contact = serializer.save()

        data = self.get_serializer(contact).data
        
        return Response(data, status=status.HTTP_201_CREATED)