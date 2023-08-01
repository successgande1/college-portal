from django.contrib.auth.models import User

from django.contrib.auth.models import AbstractUser, Group

from django.db import models
from PIL import Image
from phonenumber_field.modelfields import PhoneNumberField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, Adjust, Transpose
from imagekit.models import ProcessedImageField
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from datetime import datetime
from academics.models import *
 

#Applicant Model
class Applicant(models.Model):
    applicant = models.OneToOneField(User, on_delete = models.CASCADE, null = True)
    course_name = models.ForeignKey(CourseOfStudy, on_delete=models.CASCADE, blank=True) 
    payment_status = models.BooleanField(default=False)
    admitted = models.BooleanField(default=False)
    added_date = models.DateField(auto_now_add=True)

    

    def __str__(self):
        return f"{self.applicant}" 
    
    

class SchoolsAttended(models.Model):
    SCHOOL_CATEGORY = [
        ('PRIMARY SCHOOL ', 'PRIMARY SCHOOL'),
        ('SECONDARY SCHOOL', 'SECONDARY SCHOOL'),
        ('NCE', 'NCE'), 
        ('ND', 'ND'), 
    ]
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    school = models.CharField(max_length=20, choices=SCHOOL_CATEGORY, default=None, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()