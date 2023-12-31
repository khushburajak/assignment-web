# Generated by Django 5.0 on 2024-01-09 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0008_remove_mycourses_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImprovementArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField()),
                ('employment_status', models.CharField(choices=[('student', 'Student'), ('job-full', 'Employed Full Time'), ('job-part', 'Employed Part Time'), ('self-employed', 'Self-employed'), ('unemployed', 'Unemployed'), ('retired', 'Retired'), ('preferNo', 'Prefer not to say'), ('other', 'Other')], max_length=20)),
                ('experience_level', models.CharField(choices=[('junior', 'Junior (0-2 years experience)'), ('mid', 'Mid-level (2+ years experience)'), ('senior', 'Senior'), ('executive', 'Executive'), ('other', 'Other')], max_length=20)),
                ('course_rating', models.CharField(choices=[('excellent', 'Excellent'), ('very-good', 'Very good'), ('good', 'Good'), ('fair', 'Fair'), ('poor', 'Poor')], max_length=20)),
                ('materials_rating', models.CharField(choices=[('extremely', 'Extremely useful'), ('very', 'Very useful'), ('somewhat', 'Somewhat useful'), ('not-so', 'Not so useful'), ('no', 'No useful at all')], max_length=20)),
                ('recommend_course', models.CharField(choices=[('definitely', 'Definitely'), ('maybe', 'Maybe'), ('not-sure', 'Not sure')], max_length=20)),
                ('comments', models.TextField()),
                ('improvement_areas', models.ManyToManyField(to='course.improvementarea')),
            ],
        ),
    ]
