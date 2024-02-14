from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class customUser(AbstractUser):
    user_type = (
        ('recruiter', 'Recruiter'),
        ('jobseeker', 'JobSeeker'),
    )
    display_name=models.CharField(max_length=30)
    user_type = models.CharField(choices=user_type, max_length=20)
    

class JobModel(models.Model):
    company_name=models.CharField(max_length=100)
    job_position=models.CharField(max_length=100)
    job_place=models.CharField(max_length=100)
    job_type=models.CharField(max_length=100)
    def __str__(self):
        return self.company_name
