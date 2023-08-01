from django.db import models
from django.contrib.auth.models import User
from accounts.models import Profile
from fees.models import *


#Academic Session Model
class AcademicSession(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)
    added_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
#Semester Session Model
class Semester(models.Model):
    name = models.CharField(max_length=100)
    academic_session = models.ForeignKey(AcademicSession, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)
    added_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
#Level Session Model
class Level(models.Model):
    LEVEL_CATEGORY = [
        ('ND 1 ', 'ND 1'),
        ('ND 2', 'ND 2'),
        ('PRE-HND', 'PRE-HND'), 
        ('HND 1', 'HND 1'), 
        ('HND 2', 'HND 2'), 
    ]
    name = models.CharField(max_length=200, null=True)
    level_type = models.CharField(max_length=20, choices=LEVEL_CATEGORY, default=None, blank=True, null=True)
    fee = models.ForeignKey(Fee, on_delete=models.CASCADE)
    added_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

# Faculty Model  
class Faculty(models.Model):
    name = models.CharField(max_length=100)
    added_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
# Department Model
class Department(models.Model):
    name = models.CharField(max_length=100)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    added_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name



# Course of Study Model
class CourseOfStudy(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    added_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


# Course Unit Model
class CourseUnit(models.Model):
    name = models.CharField(max_length=100)
    credit_load = models.PositiveIntegerField()
    course_of_study = models.ForeignKey(CourseOfStudy, on_delete=models.CASCADE)
    is_core_course = models.BooleanField(default=False)
    is_elective_course = models.BooleanField(default=False)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    added_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    

# Students model
class Student(models.Model):
    candidate = models.OneToOneField(Profile, on_delete=models.CASCADE)
    academic_session = models.ForeignKey(AcademicSession, on_delete=models.CASCADE)
    course = models.ForeignKey(CourseOfStudy, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    graduated = models.BooleanField(default=False)
    added_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.candidate.name} - Level {self.level} - {self.academic_session}"
    
    def promote_to_next_level(self):
        # Logic to promote the student to the next level
        # Nigerian Polytechnics have a promotion policy like moving to the next level (e.g., 100 to 200)
        # You can implement any business rules for promotion here

        # Assuming the maximum level is 800 in this example
        if self.level < 800:
            self.level += 100
            self.save()

    def graduate(self):
        # Logic to handle student graduation
        # You can implement any business rules for graduation here

        # Assuming a student can graduate at level 800 in this example
        if self.level >= 800:
            self.graduated = True
            self.save()

# Student Course Registration
class CourseEnrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_unit = models.ForeignKey(CourseUnit, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    added_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} - {self.course_unit} - {self.semester}"
    
# academic/models.py
class CourseCarryover(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_unit = models.ForeignKey(CourseUnit, on_delete=models.CASCADE)
    previous_semester = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name='carryover_courses')
    
    def __str__(self):
        return f"{self.student} - {self.course_unit} - Carryover from {self.previous_semester}"


