# Generated by Django 5.0.1 on 2024-02-03 06:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0005_alter_studentmodel_student_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='marksmodel',
            name='credit',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='coursemodel',
            name='course_code',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='coursemodel',
            name='course_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='gradingsystem',
            name='course_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myApp.coursemodel'),
        ),
        migrations.AlterField(
            model_name='gradingsystem',
            name='student_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myApp.studentmodel'),
        ),
        migrations.AlterField(
            model_name='marksmodel',
            name='course_code',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myApp.coursemodel'),
        ),
        migrations.AlterField(
            model_name='marksmodel',
            name='student_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myApp.studentmodel'),
        ),
        migrations.AlterField(
            model_name='studentmodel',
            name='courses',
            field=models.ManyToManyField(null=True, to='myApp.coursemodel'),
        ),
        migrations.AlterField(
            model_name='studentmodel',
            name='student_id',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='studentmodel',
            name='student_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
