# Generated by Django 5.1.4 on 2025-01-08 10:57

import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
import django.db.models.deletion
import django.utils.timezone
import multiselectfield.db.fields
import phonenumber_field.modelfields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region='KG')),
                ('address', models.CharField(blank=True, max_length=64, null=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='photos_user')),
                ('gender', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('OTHER', 'OTHER')], default='MALE', max_length=32)),
                ('user_role', models.CharField(choices=[('doctor', 'doctor'), ('patient', 'patient')], default='patient', max_length=8)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='DepartmentDoctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(help_text='Отделение врача', max_length=100)),
                ('department_en', models.CharField(help_text='Отделение врача', max_length=100, null=True)),
                ('department_ru', models.CharField(help_text='Отделение врача', max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SpecialtyDoctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speciality', models.CharField(help_text='Специальность врача', max_length=100)),
                ('speciality_en', models.CharField(help_text='Специальность врача', max_length=100, null=True)),
                ('speciality_ru', models.CharField(help_text='Специальность врача', max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Wards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('name_en', models.CharField(max_length=100, null=True)),
                ('name_ru', models.CharField(max_length=100, null=True)),
                ('ward_type', models.CharField(choices=[('VIP', 'VIP'), ('STANDARD', 'STANDARD')], default='STANDARD', max_length=12)),
                ('capacity', models.PositiveIntegerField(default=5)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('userprofile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('shift_start', models.TimeField(blank=True, null=True)),
                ('shift_end', models.TimeField(blank=True, null=True)),
                ('working_days', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Mon', 'Monday'), ('Tue', 'Tuesday'), ('Wed', 'Wednesday'), ('Thu', 'Thursday'), ('Fri', 'Friday'), ('Sat', 'Saturday'), ('San', 'Sunday')], max_length=100, null=True)),
                ('status_edu', models.CharField(blank=True, choices=[('Высшее образование', 'Высшее образование'), ('Кандидат мединциских наук', 'Кандидат мединциских наук'), ('Доктор мединциских наук', 'Доктор мединциских наук')], max_length=255, null=True)),
                ('price', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctors', to='medicine.departmentdoctor')),
                ('speciality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctors', to='medicine.specialtydoctor')),
            ],
            options={
                'verbose_name': 'Doctor',
                'verbose_name_plural': 'User_Doctor',
            },
            bases=('medicine.userprofile',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='PatientProfile',
            fields=[
                ('userprofile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('emergency_contact', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('birthday', models.DateField()),
                ('allergy', models.TextField(blank=True, null=True)),
                ('allergy_en', models.TextField(blank=True, null=True)),
                ('allergy_ru', models.TextField(blank=True, null=True)),
                ('blood_type', models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default=1, max_length=1, null=True)),
            ],
            options={
                'verbose_name': 'Patient',
                'verbose_name_plural': 'User_Patient',
            },
            bases=('medicine.userprofile',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('planned', 'planned'), ('completed', 'completed'), ('cancelled', 'cancelled')], default='planned', max_length=32)),
                ('notes', models.TextField()),
                ('notes_en', models.TextField(null=True)),
                ('notes_ru', models.TextField(null=True)),
                ('doctor', models.ManyToManyField(related_name='doctors_a', to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patients_a', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True)),
                ('person', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('comment', models.TextField()),
                ('comment_en', models.TextField(null=True)),
                ('comment_ru', models.TextField(null=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedbacks_d', to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='medicine.feedback')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedbacks_p', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MedicalRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('doctor', models.ManyToManyField(related_name='doctors_records', to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_records', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images_message')),
                ('video', models.FileField(blank=True, null=True, upload_to='videos_message')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicine.chat')),
            ],
        ),
        migrations.CreateModel(
            name='Prescribed_Medication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnosis', models.TextField(blank=True, null=True)),
                ('diagnosis_en', models.TextField(blank=True, null=True)),
                ('diagnosis_ru', models.TextField(blank=True, null=True)),
                ('treatment', models.TextField(blank=True, null=True)),
                ('treatment_en', models.TextField(blank=True, null=True)),
                ('treatment_ru', models.TextField(blank=True, null=True)),
                ('prescribed_medication', models.CharField(max_length=100)),
                ('prescribed_medication_en', models.CharField(max_length=100, null=True)),
                ('prescribed_medication_ru', models.CharField(max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medications', to='medicine.medicalrecord')),
            ],
        ),
        migrations.CreateModel(
            name='Prescriptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medication_name', models.CharField(max_length=55)),
                ('dosage', models.CharField(max_length=25)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('diagnosis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medical', to='medicine.medicalrecord')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_exper', models.DateField()),
                ('end_exper', models.DateField()),
                ('description_exper', models.TextField()),
                ('description_exper_en', models.TextField(null=True)),
                ('description_exper_ru', models.TextField(null=True)),
                ('specialist_experience', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experiences', to='medicine.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_edu', models.DateField()),
                ('end_edu', models.DateField()),
                ('description_study', models.TextField()),
                ('description_study_en', models.TextField(null=True)),
                ('description_study_ru', models.TextField(null=True)),
                ('specialist_educations', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='educations', to='medicine.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Warnings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('ward', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicine.wards')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicine.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicine.patientprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Billings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.PositiveIntegerField()),
                ('paid', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='billings', to='medicine.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='billings', to='medicine.patientprofile')),
            ],
        ),
        migrations.CreateModel(
            name='FeedbackLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.BooleanField(blank=True, default=False, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('feedbacks', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedback_lakes', to='medicine.feedback')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patients', to='medicine.patientprofile')),
            ],
            options={
                'unique_together': {('patient', 'like')},
            },
        ),
    ]
