# Generated by Django 5.0.1 on 2024-02-03 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0007_rename_course_code_marksmodel_course_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marksmodel',
            name='credit',
        ),
        migrations.AddField(
            model_name='coursemodel',
            name='credit',
            field=models.IntegerField(null=True),
        ),
    ]
