
""" User Views """

# Django REST Framework
from rest_framework.decorators import action
from rest_framework import status, viewsets, mixins
from rest_framework.response import Response
from rest_framework.views import APIView

# Permissions
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)
from coeadmin.user.permissions import IsAccountOwner

# Serializers
from coeadmin.user.serializers import  ProfileModelSerializer
from coeadmin.user.serializers.user import (
    UserLoginSerializer,
    UserModelSerializer,
    UserSignUpSerializer,
)

# Models
from coeadmin.user.models import User


class UserViewSet(mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                viewsets.GenericViewSet):
    """ User view Set. """

    queryset = User.objects.filter(is_active=True , is_pollster=True)
    serializer_class = UserModelSerializer
    lookup_field = 'username'
    
    def get_permissions(self):
        """ Assing permissions based on action. """
        
        if self.action in ['signup','login']:
            permissions = [AllowAny]
        elif self.action in ['update', 'partial_update']:
            permissions = [IsAuthenticated, IsAccountOwner]
        else: 
            permissions = [IsAuthenticated]
        return [p() for p in permissions]

    @action(detail=False, methods=['post'])
    def login(self, request):
        """ User sign in. """
        
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': UserModelSerializer(user).data,
            'access_token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def signup(self, request):
        """ User sign up. """

        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['put','patch'])
    def profile(self, request, *args, **kwargs):
        """ Update profile data. """

        user = self.get_object()
        profile = user.profile
        partial = request.method == 'PATCH'
        serializer = ProfileModelSerializer(
            profile,
            data=request.data,
            partial=partial
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = UserModelSerializer(user).data
        return Response(data)