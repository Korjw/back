from django.urls import path, re_path
from api import views

urlpatterns = [
    path('emr/api/templates/', views.templates_list, name='templates_list'),
    path('emr/api/templates/<int:id>/', views.templates_detail,
         name='templates_detail'),

    path('emr/api/symptom/list/', views.SymptomsView.as_view(),
         name='symptoms_list'),

    path('emr/api/prescription/list/', views.PrescriptionsView.as_view(),
         name='prescriptions_list'),

    path('emr/api/emr/list/', views.DiagnosisView.as_view(),
         name='diagnosis_list'),

    path('emr/api/appointment/list/', views.AppointmentsView.as_view(),
         name='appointments_list'),

    path('emr/api/appointment/', views.AppointmentView.as_view(),
         name='appointment'),

    path('emr/api/patientInCharge/list/', views.PatientInChargeView.as_view(),
         name='patientInCharge_list'),

     path('emr/patient/api/appointment/', views.AppointmentsView.as_view(),
         name='a'),

     path('emr/patient/api/symptom/list', views.SymptomsViewWithDate.as_view(),
         name='b'),

     path('emr/patient/api/medicine/list/', views.PrescriptionsViewWithDate.as_view(),
         name='c'),

     path('emr/patient/api/emr/list', views.DiagnosisView.as_view(),
         name='d'),

     path('emr/patient/api/appointment/list', views.AppointmentPatientView.as_view(),
         name='e'),

    # Vue.js routing
    re_path(r'^emr/', views.HomeView.as_view(), name='home'),
]
