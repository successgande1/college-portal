from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(FeeType)

admin.site.register(Fee)

admin.site.register(ApplicantFee)


admin.site.register(StudentFee)
 