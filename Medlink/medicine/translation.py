from .models import *
from modeltranslation.translator import TranslationOptions,register


@register(SpecialtyDoctor)
class SpecialtyDoctorTranslation(TranslationOptions):
    fields = ('speciality',)


@register(DepartmentDoctor)
class DepartmentDoctorTranslation(TranslationOptions):
    fields = ('department',)



@register(Doctor)
class DoctorTranslation(TranslationOptions):
    fields = []

#
@register(MedicalRecord)
class MedicalRecordTranslation(TranslationOptions):
    fields = []

# Перевод Education
@register(Education)
class EducationTranslation(TranslationOptions):
    fields = ('description_study',)


# Перевод Experience
@register(Experience)
class ExperienceTranslation(TranslationOptions):
    fields = ('description_exper',)


# Перевод PatientProfile
@register(PatientProfile)
class PatientProfileTranslation(TranslationOptions):
    fields = ('allergy',)


# Перевод Appointment
@register(Appointment)
class AppointmentTranslation(TranslationOptions):
    fields = ('notes',)


# Перевод Prescribed_Medication
@register(Prescribed_Medication)
class PrescribedMedicationTranslation(TranslationOptions):
    fields = ('diagnosis', 'treatment', 'prescribed_medication')


# Перевод Feedback
@register(Feedback)
class FeedbackTranslation(TranslationOptions):
    fields = ('comment',)


# Перевод Wards
@register(Wards)
class WardsTranslation(TranslationOptions):
    fields = ('name',)