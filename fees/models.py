# fees/models.py
from django.db import models
from django.contrib.auth.models import User

class FeeType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

# fees model
class Fee(models.Model):
    fee_type = models.ForeignKey(FeeType, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_per_semester = models.BooleanField(default=False, help_text="Is the fee charged per semester?")
    is_per_session = models.BooleanField(default=False, help_text="Is the fee charged per academic session?")
    
    def __str__(self):
        return f"{self.fee_type} - {self.amount}"


class ApplicantFee(models.Model):
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    fee = models.ForeignKey(Fee, on_delete=models.CASCADE)
    payment_status = models.CharField(max_length=20, blank=True)
    payment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.applicant} - {self.fee}"
    
class StudentFee(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    fee = models.ForeignKey(Fee, on_delete=models.CASCADE)
    payment_status = models.CharField(max_length=20, blank=True)
    payment_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.student} - {self.fee}"
