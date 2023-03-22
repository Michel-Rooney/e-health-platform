from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('patients/', views.patients, name='patients'),
    path('patient/<str:id>/', views.patient, name='patient'),
    path('patient_chart/<str:id>/', views.patient_chart, name='patient_chart'),
    path('create_note/<str:id>/', views.create_note, name='create_note'),
    path('del_note/<str:id>/', views.del_note, name='del_note'),
    path('update_information/<str:id>/', views.update_information, name='update_information'),
    path('management/doctors/', views.management_doctors, name='management_doctors'),
    path('management/patients/', views.management_patients, name='management_patients'),
    path('management/doctors/add/', views.management_doctors_add, name='management_doctors_add'),
    path('management/doctors/remove/', views.management_doctors_remove, name='management_doctors_remove'),
    path('management/patients/add/<str:id>/', views.management_patients_add, name='management_patients_add'),
    path('management/patients/remove/<str:id>/', views.management_patients_remove, name='management_patients_remove'),
    # path('page1/', views.page1, name='page1'),
    path('page2/', views.page2, name='page2'), 
]