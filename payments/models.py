from django.db import models
from fees.models import Fee
from django.contrib.auth.models import User
from academics.models import Student
# Create your models here.

class ApplicantFee(models.Model):
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    fee = models.ForeignKey(Fee, on_delete=models.CASCADE)
    payment_status = models.CharField(max_length=20, blank=True)
    payment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.applicant} - {self.fee}"
    

    
    
class FeePayment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    fee = models.ForeignKey(Fee, on_delete=models.CASCADE)
    payment_status = models.CharField(max_length=20, blank=True)
    payment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} - {self.fee}"
