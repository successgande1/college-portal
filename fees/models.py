# fees/models.py
from django.db import models
from django.contrib.auth.models import User


class FeeType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=200, blank=True)

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




