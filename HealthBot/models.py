from django.db import models
import datetime

# Create your models here.
class Appointment(models.Model):
    SEX=(
        ('Male', 'Male'),
        ('Female', 'Female')
    )

    sex=models.CharField(max_length=200, null=True, choices=SEX)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    lastName = models.CharField(max_length=200)
    mobileNumber = models.CharField(max_length=150)
    appointmentDate = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()

    def __str__(self):
        return  self.name + self.lastName
