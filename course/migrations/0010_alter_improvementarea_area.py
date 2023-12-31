# Generated by Django 5.0 on 2024-01-09 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0009_improvementarea_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='improvementarea',
            name='area',
            field=models.CharField(choices=[('lectures', 'Lectures and videos'), ('material', 'Instructional materials i.e. readings'), ('assignments', 'Course assignments and projects'), ('exams', 'Graded assignments and exams'), ('forum', 'Forum'), ('additional-courses', 'Additional Courses')], max_length=100),
        ),
    ]
