from django.urls import path
from . import views


urlpatterns = [
    path('heart_rate/', views.heart_rate, name='heart_rate'),
]