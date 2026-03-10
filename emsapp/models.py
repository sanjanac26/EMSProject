from django.db import models
from django.core.validators import RegexValidator

phone_validator = RegexValidator(
    regex=r'^\+?\d{10,15}$',
    message="Phone number must be 10-15 digits and may include +"
)

class Employee(models.Model):
    e_id = models.AutoField(primary_key=True)
    e_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, validators=[phone_validator])
    department = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    date_joined = models.DateField()

    def __str__(self):
        return f"{self.e_id} - {self.e_name}"