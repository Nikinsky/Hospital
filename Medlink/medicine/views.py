from rest_framework import viewsets, generics, status
from .serializers import *
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .filters import *
from .pagination import *
from .permissions import *
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from .models import *
from .serializers import *




class BaseRegisterView(generics.CreateAPIView):
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class DoctorRegisterView(BaseRegisterView):
    serializer_class = DoctorRegisterSerializer

class PatientRegisterView(BaseRegisterView):
    serializer_class = PatientRegisterSerializer




class BaseCustomLoginView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.data, status=status.HTTP_200_OK)

class DoctorCustomLoginView(BaseCustomLoginView):
    serializer_class = DoctorLoginSerializer

class PatientCustomLoginView(BaseCustomLoginView):
    serializer_class = PatientLoginSerializer



class BaseLogoutView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class DoctorLogoutView(BaseLogoutView):
    pass

class PatientLogoutView(BaseLogoutView):
    pass







class UserProfileListCreateView(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class UserProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer



class SpecialtyDoctorListCreateView(generics.ListCreateAPIView):
    queryset = SpecialtyDoctor.objects.all()
    serializer_class = SpecialtyDoctorSerializer

class DepartmentDoctorListCreateView(generics.ListCreateAPIView):
    queryset = DepartmentDoctor.objects.all()
    serializer_class = DepartmentDoctorSerializer










class DoctorListView(generics.ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['first_name','last_name']
    filterset_class = DoctorFilter
    # pagination_class = DoctorPagination
    # permission_classes = [CheckDoctorTrue]

class DoctorProfileView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorProfileSerializer

    def get_queryset(self):
        return Doctor.objects.filter(id=self.request.user.id)


class DoctorDetailView(generics.RetrieveAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorDetailSerializer









class PatientProfileView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PatientProfile.objects.all()
    serializer_class = PatientProfileSerializer

    def get_queryset(self):
         return PatientProfile.objects.filter(id=self.request.user.id)


class PatientListView(generics.ListAPIView):
    queryset = PatientProfile.objects.all()
    serializer_class = PatientListSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    filterset_class = PatientFilter
    search_fields = ['first_name', 'last_name','allergies']
    pagination_class = PatientPagination


class PatientDetailView(generics.ListAPIView):
    queryset = PatientProfile.objects.all()
    serializer_class = PatientDetailSerializer












# Appointment Views
class AppointmentListCreateView(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


class AppointmentCreateView(generics.CreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class AppointmentDetailDeleteUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer




# MedicalRecord Views
class MedicalRecordListCreateView(generics.ListCreateAPIView):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer
    pagination_class = MedicalRecordPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['patient__first_name', 'patient__last_name']
    ordering_fields = ['created_at']
    filterset_class = MedicalRecordFilter
    permission_classes = [CheckDoctorTrue]



class MedicalRecordDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer

    def get_queryset(self):
        return MedicalRecord.objects.filter(patient__id=self.request.user.id)

class MedicalRecordDetailForDoctorView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer








class PrescribedMedicationListCreateView(generics.ListCreateAPIView):
    queryset = Prescribed_Medication.objects.all()
    serializer_class = PrescribedMedicationSerializer

class PrescribedMedicationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Prescribed_Medication.objects.all()
    serializer_class = PrescribedMedicationSerializer








class FeedbackListCreateView(generics.ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

class FeedbackDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

class FeedbackLikeView(generics.CreateAPIView):
    queryset = FeedbackLike.objects.all()
    serializer_class = FeedbackLikeSerializer













class PrescriptionsCreateAPIView(generics.CreateAPIView):
    queryset = Prescriptions.objects.all()
    serializer_class = PrescriptionsCreateSerializer

class PrescriptionsListAPIView(generics.ListAPIView):
    queryset = Prescriptions.objects.all()
    serializer_class = PrescriptionsListSerializer

class PrescriptionsDetailAPIView(generics.RetrieveUpdateAPIView):
    queryset = Prescriptions.objects.all()
    serializer_class = PrescriptionsDetailSerializer




class BillingsCreateAPIView(generics.CreateAPIView):
    queryset = Billings.objects.all()
    serializer_class = BillingsCreateSerializer

class BillingsListAPIView(generics.ListAPIView):
    queryset = Billings.objects.all()
    serializer_class = BillingsInfoSerializer

class WardsListAPIView(generics.ListAPIView):
    queryset = Wards.objects.all()
    serializer_class = WardsListSerializers


class WardsCreateAPIView(generics.CreateAPIView):
    queryset = Wards.objects.all()
    serializer_class = WardsCreateSerializers






# ТЗ(100%)
# + translation (+2),
# filter(),
# search(),
# ordering(),
# swagger,
# paginations
# permissions(isAuthOr, +Base...)
# register(google, github + jwt)
# req.txt
# docker > docker-compose
# github
# AWS > TG

# (.env, get_queryset, router path,
# viewset generics, inline,
# models.py + def)
#
# WEBSOCKET CHAT
# (HTTP, WEBSOCKET)