from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.



class Doctor(models.Model):
    def doctor():
        return 'doctor'
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=2000)
    password = models.CharField(max_length=50, null=False, blank=False, default=doctor)
    slug = models.SlugField()


    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-id',)

class Nurse(models.Model):
    def nurse():
        return 'nurse'
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=2000)
    password = models.CharField(max_length=50, null=False, blank=False, default=nurse)
    slug = models.SlugField()


    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-id',)   


class Patient(models.Model):
    # receptionist 
    id = models.AutoField(primary_key=True)
    Patient_name = models.CharField(max_length=100)
    Patient_age = models.IntegerField()
    Patient_Residence = models.CharField(max_length=100)
    Patient_phone = models.IntegerField()
    Patient_email = models.EmailField(max_length=100)
    # nurse
    Patient_Bp  = models.IntegerField()
    Patient_weight = models.IntegerField()
    Patient_height = models.IntegerField()
    Patient_temperature = models.IntegerField()
    # Labtech
    Patient_Inr = models.IntegerField()
    # Doctor
    Patient_Diagnosis = models.CharField(max_length=100)


    def __str__(self) -> str:
        return self.Patient_name



class INR(models.Model):
    INR_name = models.CharField(max_length=100)
    INR_Range_min = models.IntegerField()
    INR_Range_max = models.IntegerField()
    INR_Range_desc = models.CharField(max_length=100)
    INR_Rtc_period = models.CharField(max_length=100)

    def __str__(self):
        return self.INR_name






