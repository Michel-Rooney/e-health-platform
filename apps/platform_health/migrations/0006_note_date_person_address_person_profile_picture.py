# Generated by Django 4.1.7 on 2023-03-15 01:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('platform_health', '0005_alter_persondata_doctor'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='address',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='profile_picture',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='profile_picture'),
            preserve_default=False,
        ),
    ]
