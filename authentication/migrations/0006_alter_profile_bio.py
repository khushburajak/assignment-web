# Generated by Django 5.0 on 2024-01-02 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_remove_profile_address_profile_city_profile_street_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]