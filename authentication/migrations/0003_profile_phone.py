# Generated by Django 5.0 on 2024-01-01 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_profile_address_profile_full_name_profile_university_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.IntegerField(max_length=12, null=True),
        ),
    ]
