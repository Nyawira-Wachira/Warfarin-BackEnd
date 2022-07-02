from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    is_receptionist = models.BooleanField(default=False)
    is_nurse = models.BooleanField(default=False)
    is_labtech = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)



class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


    def __str__(self):
        return self.user.username
        

class Nurse(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username




class Patient(models.Model):
    # receptionist 
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



class INR_Range(models.Model):
    INR_Range_name = models.CharField(max_length=100)
    INR_Range_min = models.IntegerField()
    INR_Range_max = models.IntegerField()

    def __str__(self):
        return self.INR_Range_name




