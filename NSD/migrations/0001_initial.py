# Generated by Django 5.2.3 on 2025-06-28 15:41

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment_DB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('phone', models.CharField(max_length=20, unique=True)),
                ('programme', models.CharField(default='', max_length=200)),
                ('state', models.CharField(max_length=150)),
                ('country', models.CharField(max_length=150)),
                ('message', models.CharField(default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Client_DB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=200)),
                ('firstname', models.CharField(max_length=200)),
                ('other_name', models.CharField(max_length=200)),
                ('mother_maiden_name', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('dob', models.DateField()),
                ('blood_group', models.CharField(max_length=50)),
                ('facial_mark', models.CharField(max_length=50)),
                ('glasses', models.CharField(max_length=50)),
                ('height_in_meters', models.DecimalField(decimal_places=2, max_digits=10)),
                ('disability', models.CharField(max_length=50)),
                ('nin', models.CharField(max_length=20, unique=True)),
                ('next_of_kin_phone', models.CharField(max_length=20)),
                ('applicant_phone', models.CharField(max_length=20, unique=True)),
                ('nationality', models.CharField(max_length=150)),
                ('state_of_origin', models.CharField(max_length=200)),
                ('lga_of_origin', models.CharField(max_length=200)),
                ('place_of_birth', models.CharField(max_length=200)),
                ('occupation', models.CharField(max_length=100)),
                ('marital_status', models.CharField(max_length=20)),
                ('programme', models.CharField(max_length=150)),
                ('training_duration', models.IntegerField()),
                ('residential_address', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('profile_picture', models.ImageField(blank=True, default='clients/profile_pictures/default.jpg', null=True, upload_to='clients/profile_pictures/')),
            ],
        ),
        migrations.CreateModel(
            name='Contact_Messages_DB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Currency_DB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('code', models.CharField(max_length=10, unique=True)),
                ('rate', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Driving_Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(default='')),
                ('duration', models.IntegerField(default=0)),
                ('type', models.CharField(default='', max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(upload_to='driving_courses/')),
            ],
        ),
        migrations.CreateModel(
            name='FeedBack_DB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=150)),
                ('profile_image', models.ImageField(blank=True, default='feedback_profile_images/default.jpg', null=True, upload_to='feedback_profile_images/')),
                ('first_name', models.CharField(max_length=200)),
                ('course_type', models.CharField(max_length=150)),
                ('profession', models.CharField(max_length=150)),
                ('location', models.CharField(max_length=200)),
                ('feedback', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Newsletter_DB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(default='', max_length=255, unique=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='State_DB',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('states', models.CharField(default='', max_length=200, unique=True)),
                ('capitals', models.CharField(default='', max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Swimming_Client_DB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=200)),
                ('firstname', models.CharField(max_length=200)),
                ('other_name', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('dob', models.DateField()),
                ('next_of_kin_phone', models.CharField(max_length=20)),
                ('applicant_phone', models.CharField(max_length=20, unique=True)),
                ('previous_experience', models.CharField(max_length=100)),
                ('health_status', models.CharField(max_length=150)),
                ('residential_address', models.CharField(max_length=500)),
                ('programme', models.CharField(max_length=150)),
                ('training_duration', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Swimming_Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('duration', models.IntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(upload_to='swimming_courses/')),
            ],
        ),
        migrations.CreateModel(
            name='Driving_Course_Identity_DB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_identity_number', models.CharField(max_length=200, unique=True)),
                ('course_name', models.CharField(max_length=200, unique=True)),
                ('type', models.CharField(default='', max_length=200)),
                ('couse_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_identity', to='NSD.driving_courses')),
            ],
        ),
        migrations.CreateModel(
            name='LGA_DB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lga', models.CharField(default='', max_length=500)),
                ('state', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lgas', to='NSD.state_db')),
            ],
        ),
    ]
