# Generated by Django 5.0.1 on 2024-02-03 04:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0003_studentmodel_subjectmodel_grademodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='courseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_code', models.CharField(max_length=20)),
                ('course_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='gradingSystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100)),
                ('course_name', models.CharField(max_length=100)),
                ('cgpa', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='studentmodel',
            old_name='name',
            new_name='student_name',
        ),
        migrations.AddField(
            model_name='studentmodel',
            name='student_id',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='studentmodel',
            name='courses',
            field=models.ManyToManyField(to='myApp.coursemodel'),
        ),
        migrations.CreateModel(
            name='marksModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.IntegerField()),
                ('course_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.coursemodel')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.studentmodel')),
            ],
        ),
        migrations.DeleteModel(
            name='gradeModel',
        ),
        migrations.DeleteModel(
            name='subjectModel',
        ),
    ]