import uuid
from django.db import models
from user.models import User


class PaitentProfile(models.Model):


	# reception
	full_name = models.CharField(max_length=50, unique=False,default="Full name")
	age = models.PositiveIntegerField(default=20)
	residence = models.CharField(max_length=50, unique=False, default="Kenya")
	email = models.EmailField(max_length=255, unique=True,default="patient@gmail.com")
	phone_number = models.CharField(max_length=10, unique=True,blank=False, default="0723467890")
	
	# nurse

	bp = models.PositiveIntegerField(default=21)
	temparature = models.PositiveIntegerField(default=37)
	height = models.CharField(max_length=50, default="1.75m")
	weight =models.CharField(max_length=50, default="60 kgs")

	# lab tech

	inr_range = models.PositiveIntegerField(null=False, default=2.4)

	

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
	username = models.CharField(max_length=50, unique=False)
	first_name = models.CharField(max_length=50, unique=False,default='firstname')
	last_name = models.CharField(max_length=50, unique=False,default='lastname')
	phone_number = models.CharField(max_length=10,default='12345678')
	GENDER_CHOICES = (
		('M', 'Male'),
		('F', 'Female'),
	)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES ,default='M')


	class Meta:
		'''
		to set table name in database
		'''
		db_table = "doctor_profile"


class NurseProfile(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='nurse_profile')
	username = models.CharField(max_length=50, unique=False)
	first_name = models.CharField(max_length=50, unique=False,default='firstname')
	last_name = models.CharField(max_length=50, unique=False,default='lastname')
	phone_number = models.CharField(max_length=10,default='12345678')
	GENDER_CHOICES = (
		('M', 'Male'),
		('F', 'Female'),
	)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES ,default='M')


	class Meta:
		'''
		to set table name in database
		'''
		db_table = "nurse_profile"


# labtech 

class LabtechProfile(models.Model):

	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='labtech_profile')
	username = models.CharField(max_length=50, unique=False)
	first_name = models.CharField(max_length=50, unique=False,default='firstname')
	last_name = models.CharField(max_length=50, unique=False,default='lastname')
	phone_number = models.CharField(max_length=10,default='12345678')
	GENDER_CHOICES = (
		('M', 'Male'),
		('F', 'Female'),
	)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES ,default='M')
	

	class Meta:
		'''
		to set table name in database
		'''
		db_table = "labtech_profile"

# reception

class ReceptionProfile(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='reception_profile')
	username = models.CharField(max_length=50, unique=False)
	first_name = models.CharField(max_length=50, unique=False,default='firstname')
	last_name = models.CharField(max_length=50, unique=False,default='lastname')
	phone_number = models.CharField(max_length=10,default='12345678')
	GENDER_CHOICES = (
		('M', 'Male'),
		('F', 'Female'),
	)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES ,default='M')
	

	class Meta:
		'''
		to set table name in database
		'''
		db_table = "reception_profile"
