# Generated by Django 4.1.7 on 2023-03-20 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('platform_health', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='profile_picture',
            field=models.ImageField(default='https://i.ibb.co/R2GHhkn/profile-default.png', upload_to='profile_picture'),
        ),
    ]
