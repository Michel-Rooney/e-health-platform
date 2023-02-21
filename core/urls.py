from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('apps.authentication.urls')),
    path('arduino/', include('apps.arduino.urls')),
    path('', include('apps.platform_health.urls')),
]
