#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from rest_framework import status
from rest_framework.generics import RetrieveAPIView,UpdateAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from user.serializers import DoctorRegistrationSerializer,PaitentRegistrationSerializer,LabTechRegistrationSerializer,ReceptionRegistrationSerializer,NurseRegistrationSerializer
from userprofile.models import LabtechProfile, PaitentProfile,DoctorProfile,NurseProfile, ReceptionProfile
from user.models import User

class UserProfileView(RetrieveAPIView):

	permission_classes = (IsAuthenticated,)
	authentication_class = JSONWebTokenAuthentication

	
	


	def get(self, request):
		try:
			
			if request.user.is_paitent == True:
				user_profile = PaitentProfile.objects.get(user=request.user)
				status_code = status.HTTP_200_OK
				response = {
					'success': 'true',
					'status code': status_code,
					'message': 'Paitent profile fetched successfully',
					'data': [{
						'first_name': user_profile.first_name,
						'last_name': user_profile.last_name,
						'phone_number': user_profile.phone_number,
						'age': user_profile.age,
						'gender': user_profile.gender,
						'case':user_profile.case,
					}]
				}
				
			if request.user.is_labtech == True:
				user_profile = LabtechProfile.objects.get(user=request.user)
				status_code = status.HTTP_200_OK
				response = {
				'success': 'true',
				'status code': status_code,
				'message': 'mme Lab profile fetched successfully',
				'data': [{
					'username': user_profile.username,
						'email': user_profile.user.email,
						'first_name':user_profile.first_name,
						'last_name':user_profile.last_name,
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
					'username': user_profile.username,
						'email': user_profile.user.email,
						'first_name':user_profile.first_name,
						'last_name':user_profile.last_name,
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
						'username': user_profile.username,
						'email': user_profile.user.email,
						'first_name':user_profile.first_name,
						'last_name':user_profile.last_name,
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
						'username': user_profile.username,
						'email': user_profile.user.email,
						'first_name':user_profile.first_name,
						'last_name':user_profile.last_name,
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




	
				    
			

















			 
