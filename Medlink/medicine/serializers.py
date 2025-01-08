from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework_simplejwt.tokens import RefreshToken
from .models import *


class DoctorRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ('username', 'first_name', 'last_name',  'password', 'gender', 'phone_number', 'department', 'speciality', 'user_role')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Doctor.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }



class PatientRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientProfile
        fields = ('username', 'first_name', 'last_name',  'password', 'gender', 'phone_number', 'birthday')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = PatientProfile.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }



# Base Login Serializer
class BaseLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


# Teacher Login Serializer
class DoctorLoginSerializer(BaseLoginSerializer):
    pass


# Student Login Serializer
class PatientLoginSerializer(BaseLoginSerializer):
    pass





class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'password']




class SpecialtyDoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialtyDoctor
        fields = ['id', 'speciality']

class DepartmentDoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartmentDoctor
        fields = ['id', 'department']











class EducationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ['start_edu', 'end_edu', 'description_study']

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ['start_exper', 'end_exper', 'description_exper']






class DoctorProfileSerializer(serializers.ModelSerializer):
    shift_start = serializers.TimeField('%H:%M')
    shift_end = serializers.TimeField('%H:%M')
    educations = EducationsSerializer(many=True)
    experiences = ExperienceSerializer(many=True)
    class Meta:
        model = Doctor
        fields = [
            'username', 'first_name', 'last_name', 'email', 'phone_number',  'picture',
            'speciality', 'department', 'shift_start', 'shift_end', 'working_days', 'status_edu',
            'price', 'educations', 'experiences', 'password'
        ]

    def update(self, instance, validated_data):
        # Обновление speciality
        speciality_data = validated_data.pop('speciality', None)
        if speciality_data:
            speciality_instance = instance.speciality
            for attr, value in speciality_data.items():
                setattr(speciality_instance, attr, value)
            speciality_instance.save()

        # Обновление department
        department_data = validated_data.pop('department', None)
        if department_data:
            department_instance = instance.department
            for attr, value in department_data.items():
                setattr(department_instance, attr, value)
            department_instance.save()

        # Обновление других полей
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance

class DoctorListSerializer(serializers.ModelSerializer):
    shift_start = serializers.TimeField('%H:%M')
    shift_end = serializers.TimeField('%H:%M')

    class Meta:
        model = Doctor
        fields = [ 'id',
            'first_name', 'last_name', 'email', 'phone_number', 'picture',
            'speciality', 'department', 'shift_start', 'shift_end', 'working_days',
            'price'
        ]

class DoctorDetailSerializer(serializers.ModelSerializer):
    shift_start = serializers.TimeField('%H:%M')
    shift_end = serializers.TimeField('%H:%M')

    class Meta:
        model = Doctor
        fields = [
            'first_name', 'last_name', 'email', 'phone_number',  'picture',
            'speciality', 'department', 'shift_start', 'shift_end', 'working_days', 'status_edu',
             'price', 'educations', 'experiences',
        ]




class DoctorSimpleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['first_name', 'last_name']






class PatientProfileSimpleSerializers(serializers.ModelSerializer):
    class Meta:
        model = PatientProfile
        fields = ['first_name', 'last_name', 'email', 'picture', 'phone_number']


class PatientProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientProfile
        fields = ['username', 'first_name', 'email', 'last_name', 'picture', 'phone_number', 'emergency_contact', 'blood_type', 'password']

class PatientListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientProfile
        fields = ['id','first_name', 'email', 'last_name', 'picture', 'emergency_contact']

class PatientDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientProfile
        fields = ['username', 'first_name', 'email', 'last_name', 'picture', 'phone_number', 'emergency_contact', 'blood_type']





class AppointmentSerializer(serializers.ModelSerializer):
    patient = PatientProfileSimpleSerializers()
    doctor = DoctorSimpleSerializers(many=True)
    date_time = serializers.DateTimeField('%H:%M %y-%m-%d')

    class Meta:
        model = Appointment
        fields = ['id', 'patient', 'doctor', 'date_time', 'status']


class MedicalRecordSerializer(serializers.ModelSerializer):
    patient = UserProfileSerializer()
    doctor = DoctorSimpleSerializers(many=True)
    created_at = serializers.DateTimeField('%H:%M %y-%m-%d')

    class Meta:
        model = MedicalRecord
        fields = ['id', 'patient', 'doctor', 'created_at']


class PrescribedMedicationSerializer(serializers.ModelSerializer):
    record = MedicalRecordSerializer()
    class Meta:
        model = Prescribed_Medication
        fields = ['id', 'record', 'prescribed_medication']













class FeedbackLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackLike
        fields = ['patient', 'feedbacks', 'like', 'created_at']


class FeedbackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Feedback
        fields = ['id', 'doctor', 'patient', 'rating', 'comment']






class PrescriptionsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescriptions
        fields = ['medication_name',
                  'dosage','diagnosis']


class PrescriptionsListSerializer(serializers.ModelSerializer):

    created_at = serializers.DateTimeField(format('%d-%m-%Y %H:%M'))
    class Meta:
        model = Prescriptions
        fields = ['medication_name','dosage',
                  'created_at']


class PrescriptionsDetailSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format('%d-%m-%Y %H:%M'))
    class Meta:
        model = Prescriptions
        fields = ['medication_name',
                  'dosage','diagnosis','created_at']







class BillingsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Billings
        fields = ['patient_id','doctor_id','total_amount','paid']


class BillingsInfoSerializer(serializers.ModelSerializer):
    patient = PatientProfileSimpleSerializers()
    class Meta:
        model = Billings
        fields = ['patient','total_amount','paid','date']




class WardsListSerializers(serializers.ModelSerializer):
    patients = PatientProfileSimpleSerializers(read_only=True, many=True)
    class Meta:
        model = Wards
        fields = '__all__'


class WardsCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Wards
        fields = '__all__'
