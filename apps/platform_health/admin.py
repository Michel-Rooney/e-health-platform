from django.contrib import admin
from apps.platform_health.models import Note, Person, PersonData


admin.site.register(Note)
admin.site.register(Person)
admin.site.register(PersonData)