from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin, TranslationInlineModelAdmin 

@admin.register(DepartmentDoctor, SpecialtyDoctor)
class DepartmentDoctorAndSpecialAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }




class EducationInline(TranslationInlineModelAdmin,admin.TabularInline):
    model = Education
    extra = 1


class ExperienceInline(TranslationInlineModelAdmin,admin.TabularInline):
    model = Experience
    extra = 1



@admin.register(Doctor)
class DoctorAdmin(TranslationAdmin):
    inlines = [EducationInline,ExperienceInline]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }




class Prescribed_MedicationInlines(TranslationInlineModelAdmin,admin.TabularInline):
    model = Prescribed_Medication
    extra = 1

@admin.register(MedicalRecord)
class MedicalRecordAdmin(TranslationAdmin):
    inlines = [Prescribed_MedicationInlines]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }



@admin.register(Feedback,Wards,Appointment)
class FeedbackAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


admin.site.register(UserProfile)
admin.site.register(PatientProfile)
admin.site.register(Prescriptions)
admin.site.register(Billings)
admin.site.register(Warnings)