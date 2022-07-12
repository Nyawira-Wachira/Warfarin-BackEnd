#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from rest_framework import status
from rest_framework.generics import RetrieveAPIView,UpdateAPIView,ListAPIView,DestroyAPIView,CreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from user.serializers import PaitentAddSerializer,InrAddSerializer, DoctorRegistrationSerializer,LabTechRegistrationSerializer,ReceptionRegistrationSerializer,NurseRegistrationSerializer
from userprofile.models import LabtechProfile, InrRangeProfile,PaitentProfile,DoctorProfile,NurseProfile, ReceptionProfile
from user.models import User

class UserProfileView(RetrieveAPIView):

	permission_classes = (IsAuthenticated,)
	authentication_class = JSONWebTokenAuthentication

	
	


	def get(self, request):
		try:
				
			if request.user.is_labtech == True:
				user_profile = LabtechProfile.objects.get(user=request.user)
				status_code = status.HTTP_200_OK
				response = {
				'success': 'true',
				'status code': status_code,
				'message': 'mme Lab profile fetched successfully',
				'data': [{
					'full_name': user_profile.full_name,
						'email': user_profile.user.email,
						
						'phone_number':user_profile.phone_number,
						'gender':user_profile.gender,
					
				}]
			}


			if request.user.is_receptionist == True:
				user_profile = ReceptionProfile.objects.get(user=request.user)
				status_code = status.HTTP_200_OK
				response = {
				'success': 'true',
				'status code': status_code,
				'message': 'Receptionist profile fetched successfully',
				'data': [{
					'full_name': user_profile.full_name,
						'email': user_profile.user.email,
						
						'phone_number':user_profile.phone_number,
						'gender':user_profile.gender,
					
				}]
			}

			if request.user.is_nurse == True:
				user_profile = NurseProfile.objects.get(user=request.user)
				status_code = status.HTTP_200_OK
				response = {
					'success': 'true',
					'status code': status_code,
					'message': 'Nurse profile fetched successfully',
					'data': [{
						'full_name': user_profile.full_name,
						'email': user_profile.user.email,
						
						'phone_number':user_profile.phone_number,
						'gender':user_profile.gender,
						
					}]
				}
			if request.user.is_doctor == True:
				user_profile = DoctorProfile.objects.get(user = request.user)
				status_code = status.HTTP_200_OK
				response = {
					'success': 'true',
					'status code': status_code,
					'message': 'Doctor profle fetched successfully',
					'data': [{
						'full_name': user_profile.full_name,
						'email': user_profile.user.email,
						
						'phone_number':user_profile.phone_number,
						'gender':user_profile.gender,
						
						}]
				}
			if request.user.is_superuser == True:
				user_profile = User.objects.get(user = request.user)
				status_code = status.HTTP_200_OK
				response = {
					'success': 'true',
					'status code': status_code,
					'message': 'Admin profile fetched successfully',
					'data': [{
						'email': user_profile.email,
					}]
				}

		except Exception as e:
			status_code = status.HTTP_400_BAD_REQUEST
			response = {
				'success': 'false',
				'status code': status.HTTP_400_BAD_REQUEST,
				'message': 'User does not exists',
				'error': str(e)
				}
		return Response(response, status=status_code)




				    
			
class ListPatientAPIView(ListAPIView):

	permission_classes = (IsAuthenticated,)
	authentication_class = JSONWebTokenAuthentication
	"""This endpoint list all of the available Patient from the database"""
	queryset = PaitentProfile.objects.all()
	serializer_class = PaitentAddSerializer

class CreatePatientAPIView(CreateAPIView):
	permission_classes = (IsAuthenticated,)
	authentication_class = JSONWebTokenAuthentication
	"""This endpoint allows for creation of a Patient"""
	queryset = PaitentProfile.objects.all()
	serializer_class = PaitentAddSerializer

class UpdatePatientAPIView(UpdateAPIView):
	permission_classes = (IsAuthenticated,)
	authentication_class = JSONWebTokenAuthentication
	"""This endpoint allows for updating a specificPatient by passing in the id of the Patient to update"""
	queryset = PaitentProfile.objects.all()
	serializer_class = PaitentAddSerializer


class DeletePatientAPIView(DestroyAPIView):
	permission_classes = (IsAuthenticated,)
	authentication_class = JSONWebTokenAuthentication
	"""This endpoint allows for deletion of a specific Patient from the database"""
	queryset = PaitentProfile.objects.all()
	serializer_class = PaitentAddSerializer

#  Inr 


			
class ListInrRangeAPIView(ListAPIView):

	permission_classes = (IsAuthenticated,)
	authentication_class = JSONWebTokenAuthentication
	"""This endpoint list all of the available Patient from the database"""
	queryset = InrRangeProfile.objects.all()
	serializer_class = InrAddSerializer

class CreateInrRangeAPIView(CreateAPIView):
	permission_classes = (IsAuthenticated,)
	authentication_class = JSONWebTokenAuthentication
	"""This endpoint allows for creation of a Patient"""
	queryset = InrRangeProfile.objects.all()
	serializer_class = InrAddSerializer

class UpdateInrRangeAPIView(UpdateAPIView):
	permission_classes = (IsAuthenticated,)
	authentication_class = JSONWebTokenAuthentication
	"""This endpoint allows for updating a specificPatient by passing in the id of the Patient to update"""
	queryset = InrRangeProfile.objects.all()
	serializer_class = InrAddSerializer


class DeleteInrRangeAPIView(DestroyAPIView):
	permission_classes = (IsAuthenticated,)
	authentication_class = JSONWebTokenAuthentication
	"""This endpoint allows for deletion of a specific Patient from the database"""
	queryset = InrRangeProfile.objects.all()
	serializer_class = InrAddSerializer
























			 
