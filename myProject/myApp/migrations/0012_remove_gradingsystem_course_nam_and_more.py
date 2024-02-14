# Generated by Django 5.0.1 on 2024-02-03 07:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0011_remove_gradingsystem_course_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gradingsystem',
            name='course_nam',
        ),
        migrations.RemoveField(
            model_name='gradingsystem',
            name='student_nam',
        ),
        migrations.AddField(
            model_name='gradingsystem',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myApp.coursemodel'),
        ),
        migrations.AddField(
            model_name='gradingsystem',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myApp.studentmodel'),
        ),
    ]