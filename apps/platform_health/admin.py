from django.contrib import admin
from apps.platform_health.models import Note, Person


admin.site.register(Note)
admin.site.register(Person)