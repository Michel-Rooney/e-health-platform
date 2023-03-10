# Generated by Django 4.1.7 on 2023-02-18 04:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('arduino', '0001_initial'),
        ('platform_health', '0002_remove_patient_notes_patient_notes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.FloatField()),
                ('weight', models.FloatField()),
                ('code', models.CharField(max_length=256)),
                ('level', models.CharField(choices=[('A', 'Admin'), ('D', 'Doctor'), ('P', 'Patients')], max_length=1)),
                ('beats', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arduino.beats')),
                ('notes', models.ManyToManyField(to='platform_health.note')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='patient',
            name='notes',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='user',
        ),
        migrations.DeleteModel(
            name='Level',
        ),
        migrations.DeleteModel(
            name='Patient',
        ),
    ]
