# Generated by Django 4.1.7 on 2023-02-18 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arduino', '0001_initial'),
        ('platform_health', '0004_remove_person_beats_remove_person_height_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persondata',
            name='beats',
        ),
        migrations.AlterField(
            model_name='persondata',
            name='notes',
            field=models.ManyToManyField(blank=True, to='platform_health.note'),
        ),
        migrations.AddField(
            model_name='persondata',
            name='beats',
            field=models.ManyToManyField(blank=True, to='arduino.beats'),
        ),
    ]
