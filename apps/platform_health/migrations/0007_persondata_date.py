# Generated by Django 4.1.7 on 2023-03-15 02:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('platform_health', '0006_note_date_person_address_person_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='persondata',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
