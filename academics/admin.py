from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(AcademicSession)

admin.site.register(Semester)

admin.site.register(Level)


admin.site.register(Faculty)

admin.site.register(Department)

admin.site.register(CourseOfStudy)

admin.site.register(CourseUnit)

admin.site.register(Student)

admin.site.register(CourseEnrollment)

admin.site.register(CourseCarryover)