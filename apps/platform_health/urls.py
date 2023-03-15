from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('patients/', views.patients, name='patients'),
    path('patient/<str:id>', views.patient, name='patient'),
    # path('page1/', views.page1, name='page1'),
    # path('page2/', views.page2, name='page2'),
]