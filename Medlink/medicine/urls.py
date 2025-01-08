from django.urls import path, include
from rest_framework import routers

from .views import *


router = routers.DefaultRouter()
# router.register(r'doctor_', DoctorDetailView, basename='doctor-reg')


urlpatterns = [
    path('', include(router.urls)),
    path('register_doctor/', DoctorRegisterView.as_view(), name='register'),
    path('login_doctor/', DoctorCustomLoginView.as_view(), name='login'),
    path('logout_doctor/', DoctorLogoutView.as_view(), name='logout'),

    path('register_patient/', PatientRegisterView.as_view(), name='register'),
    path('login_patient/', PatientCustomLoginView.as_view(), name='login'),
    path('logout_patient/', PatientLogoutView.as_view(), name='logout'),


    path('doctor_profile/<int:pk>/', DoctorProfileView.as_view(), name='doctor-profile'),
    path('doctor_list', DoctorListView.as_view(), name='doctor_list'),
    path('doctor_detail/<int:pk>/', DoctorDetailView.as_view(), name='doctor_detail'),

    path('patient_profile/<int:pk>/', PatientProfileView.as_view(), name='patient-profile'),
    path('patient_list', PatientListView.as_view(), name='patient_list'),
    path('patient_detail/<int:pk>/', PatientDetailView.as_view(), name='patient_detail'),

    path('appointment_list', AppointmentListCreateView.as_view(), name='appointment_list'),
    path('appointment_create', AppointmentCreateView.as_view(), name='appointment_create'),
    path('appointment_detail/<int:pk>/', AppointmentDetailDeleteUpdateAPIView.as_view(), name='appointment_detail'),

    path('medical_record_list', MedicalRecordListCreateView.as_view(), name='medical_record_list'),
    path('medical_record_detail/<int:pk>/', MedicalRecordDetailView.as_view(), name='medical_record_detail'),
    path('medical_record_for_doctor_detail/<int:pk>/', MedicalRecordDetailForDoctorView.as_view(), name='medical_record_for_doctor_detail'),

    path('feedback_list', FeedbackListCreateView.as_view(), name='feedback_list'),
    path('feedback/<int:pk>/', FeedbackDetailView.as_view(), name='feedback_detail'),
    path('feedback_like_list', FeedbackLikeView.as_view(), name='feedback_like-list'),

    path('prescription_list/', PrescriptionsListAPIView.as_view(), name='prescription_list'),
    path('prescription_detail/<int:pk>/', PrescriptionsDetailAPIView.as_view(), name='prescription_delete_update'),
    path('prescription_create/', PrescriptionsCreateAPIView.as_view(), name='prescription_list'),

    path('billings_create_list/', BillingsListAPIView.as_view(), name='billings_create_list'),
    path('billings_create_detail/<int:pk>/', BillingsCreateAPIView.as_view(), name='billings_detail'),

    path('wards_list/', WardsListAPIView.as_view(), name='departments'),
    path('wards_create/', WardsCreateAPIView.as_view(), name='departments'),

]