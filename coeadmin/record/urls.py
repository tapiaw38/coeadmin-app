""" Record URLs. """

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import record as record_views
from .views import person as person_views
from .views import contact as contact_views


router = DefaultRouter()
router.register(r'persons', person_views.PersonViewSet, basename='persons')
router.register(r'record', record_views.RecordViewSet, basename='record')
router.register(
    r'record/(?P<id>[0-9]+)/contacts', 
    contact_views.ContactViewSet,
    basename='record-contacts'
)

urlpatterns = [] + router.urls
