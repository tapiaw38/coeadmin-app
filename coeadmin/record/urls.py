""" Record URLs. """

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import record as record_views

router = DefaultRouter()
router.register(r'persons', record_views.PersonViewSet, basename='persons')
router.register(r'record', record_views.RecordViewSet, basename='record')

urlpatterns = [] + router.urls
