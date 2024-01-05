# Generated by Django 5.0 on 2024-01-05 06:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctor', '0003_delete_doctor_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('special', models.CharField(choices=[('Cardiology', 'Cardiology'), ('Skin Care', 'Skin Care'), ('Pediatrics', 'Pediatrics')], max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phoneno', models.CharField(max_length=255)),
                ('degree', models.CharField(max_length=255)),
                ('y_of_exp', models.IntegerField()),
                ('address', models.TextField(max_length=500)),
                ('password', models.CharField(max_length=255)),
                ('profile_pic', models.FileField(default='sad.jpg', upload_to='patient_profiles')),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Doctor.departmenttable')),
            ],
        ),
    ]
