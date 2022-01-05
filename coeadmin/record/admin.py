# Django
from django.contrib import admin

# Models
from coeadmin.record.models import (
    Person,
    Positive,
    Contact,
    Isolation,
    Location
)

admin.site.register(Person)
admin.site.register(Positive)
admin.site.register(Contact)
admin.site.register(Isolation)
admin.site.register(Location)