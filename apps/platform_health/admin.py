from django.contrib import admin
from apps.platform_health.models import Note, Person, PersonData, Doctor


admin.site.register(Note)
admin.site.register(Doctor)
admin.site.register(Person)
admin.site.register(PersonData)