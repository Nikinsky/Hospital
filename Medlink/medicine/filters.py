from django_filters.rest_framework import FilterSet
from .models import *


class DoctorFilter(FilterSet):
    class Meta:
        model = Doctor
        fields = {
            'speciality': ['exact'],
            'department': ['exact'],
            'shift_start': ['gt', 'lt'],
            'shift_end': ['gt', 'lt'],
            'working_days': ['exact'],
            'status_edu': ['exact'],
            'price': ['gt', 'lt']
        }


class PatientFilter(FilterSet):
    class Meta:
        model = PatientProfile
        fields = {
            'blood_type': ['exact'],
            'birthday': ['gt', 'lt'],


        }


class MedicalRecordFilter(FilterSet):
    class Meta:
        model = MedicalRecord
        fields = {
            'created_at': ['gt', 'lt'],
        }






