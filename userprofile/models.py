
import uuid
from django.db import models
from user.models import User


class PaitentProfile(models.Model):

	# reception
	full_name = models.CharField(max_length=50, unique=False,default="")
	age = models.PositiveIntegerField(default=0)
	residence = models.CharField(max_length=50, unique=False, default="")
	email = models.EmailField(max_length=255, unique=True,default="")
	phone_number = models.CharField(max_length=10, unique=True,blank=False, default="")
	
	# nurse

	bp = models.CharField(max_length=100,default="")
	temparature = models.PositiveIntegerField(default=0)
	height = models.CharField(max_length=50, default="")
	weight =models.CharField(max_length=50, default="")

	# lab tech

	inr_range = models.PositiveIntegerField(default=0)
	
	# default 

	currency_dose =models.CharField(max_length=50, default="5 mg")

	
	

	# doctor 

	diagnosis = models.CharField(max_length=50, default="Continue with the previous dose of ...  RTC 2 to 4 Weeks")

	class Meta:
		'''
		to set table name in database
		'''
		db_table = "paitent_profile"

class DoctorProfile(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor_profile')
	full_name = models.CharField(max_length=50, unique=False)
	phone_number = models.CharField(max_length=10,default='')
	GENDER_CHOICES = (
		('M', 'Male'),
		('F', 'Female'),
	)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES ,default='')


	class Meta:
		'''
		to set table name in database
		'''
		db_table = "doctor_profile"


class NurseProfile(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='nurse_profile')
	full_name = models.CharField(max_length=50, unique=False)
	phone_number = models.CharField(max_length=10,default='')
	GENDER_CHOICES = (
		('M', 'Male'),
		('F', 'Female'),
	)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES ,default='')


	class Meta:
		'''
		to set table name in database
		'''
		db_table = "nurse_profile"


# labtech 

class LabtechProfile(models.Model):

	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='labtech_profile')
	full_name = models.CharField(max_length=50, unique=False)
	phone_number = models.CharField(max_length=10,default='')
	GENDER_CHOICES = (
		('M', 'Male'),
		('F', 'Female'),
	)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES ,default='')
	

	class Meta:
		'''
		to set table name in database
		'''
		db_table = "labtech_profile"

# reception

class ReceptionProfile(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='reception_profile')
	full_name = models.CharField(max_length=50, unique=False)
	phone_number = models.CharField(max_length=10,default='')
	GENDER_CHOICES = (
		('M', 'Male'),
		('F', 'Female'),
	)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES ,default='')

	class Meta:


		db_table = "reception_profile"



# Inr Range 


class InrRangeProfile(models.Model):
	inr_protocol = models.CharField(max_length=50,unique=False,default='')
	inr_range = models.CharField(max_length=100,default="0")
	remedy = models.CharField(max_length=500,default="")
	return_to_clinc =models.CharField(max_length=50,default="")
	

	class Meta:

		db_table = "inrrange_profile"


	
	
	

