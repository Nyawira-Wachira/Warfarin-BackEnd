import uuid
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
	'''
	creating a manager for a custom user model
	https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#writing-a-manager-for-a-custom-user-model
	'''
	def create_user(self, email, password=None):
		"""
		Create and return a `User` with an email, username and password.
		"""
		if not email:
			raise ValueError('Users Must Have an email address')

		user = self.model(
			email=self.normalize_email(email),
		)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, password):
		"""
		Create and return a `User` with superuser (admin) permissions.
		"""
		if password is None:
			raise TypeError('Superusers must have a password.')

		user = self.create_user(email)
		user.set_password(password)
		user.is_superuser = True
		user.is_staff = True
		user.save()
		return user

	def create_paitentuser(self,email,password):
		if password is None:
			raise TypeError('Paitent must have a password')
		user = self.create_user(email)
		user.set_password(password)
		user.is_paitent = True
		user.save()
		return user

	# receptonist
	def create_receptionistuser(self,email,password):
		if password is None:
			raise TypeError('Receptionist must have a password')
		user = self.create_user(email)
		user.set_password(password)
		user.is_receptionist = True
		user.save()
		return user

	# lab tech
	def create_labtechuser(self,email,password):
		if password is None:
			raise TypeError('Lab tech must have a password')
		user = self.create_user(email)
		user.set_password(password)
		user.is_labtech = True
		user.save()
		return user


	def create_doctoruser(self,email,password):
		if password is None:
			raise TypeError('Doctors must have a password')
		user = self.create_user(email)
		user.set_password(password)
		user.is_doctor = True
		user.save()
		return user
	# nurse
	def create_nurseuser(self,email,password):
		if password is None:
			raise TypeError('Nurse must have a password')
		user = self.create_user(email)
		user.set_password(password)
		user.is_nurse = True
		user.save()
		return user
#admin
	def create_adminuser(self,email,password):
			if password is None:
				raise TypeError('admin must have a password')
			user = self.create_user(email)
			user.set_password(password)
			user.is_admin = True
			user.save()
			return user
		
class User(AbstractBaseUser):

	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	email = models.EmailField(
		verbose_name='email address',
		max_length=255,
		unique=True
	)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)
	is_paitent = models.BooleanField(default=False)
	is_doctor = models.BooleanField(default=False)
	is_nurse = models.BooleanField(default=False)
	is_receptionist = models.BooleanField(default=False)
	is_labtech = models.BooleanField(default=False)
	is_admin = models.BooleanField(default=False)
	
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	# Tells Django that the UserManager class defined above should manage
	# objects of this type.
	objects = UserManager()

	def __str__(self):
		return self.email

class Meta:
	'''
	to set table name in database
	'''
	db_table = "login"
