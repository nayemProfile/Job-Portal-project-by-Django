# Generated by Django 5.0.1 on 2024-02-03 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0006_marksmodel_credit_alter_coursemodel_course_code_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='marksmodel',
            old_name='course_code',
            new_name='course_name',
        ),
        migrations.RenameField(
            model_name='marksmodel',
            old_name='student_id',
            new_name='student_name',
        ),
    ]
