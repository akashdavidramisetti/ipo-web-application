from django.db import models

# Create your models here.
from django.db import models

class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()  # Date of birth
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
