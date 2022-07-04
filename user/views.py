#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib import response
from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from user.serializers import LabTechRegistrationSerializer, PaitentRegistrationSerializer,DoctorRegistrationSerializer,NurseRegistrationSerializer, ReceptionRegistrationSerializer
from user.serializers import UserLoginSerializer
from user.models import User






# labtech

class LabTechRegistrationView(CreateAPIView):
    serializer_class = LabTechRegistrationSerializer
    permission_classes = (AllowAny,)
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message': 'Lab tech registered  successfully',
            }
        status_code = status.HTTP_200_OK
        return Response(response, status=status_code)


# receptionist
class ReceptionistRegistrationView(CreateAPIView):
    serializer_class = ReceptionRegistrationSerializer
    permission_classes = (AllowAny,)
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message': 'Receptionist registered  successfully',
            }
        status_code = status.HTTP_200_OK
        return Response(response, status=status_code)



class PaitentRegistrationView(CreateAPIView):

    serializer_class = PaitentRegistrationSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message': 'Paitent registered  successfully',
            }
        status_code = status.HTTP_200_OK
        return Response(response, status=status_code)

class DoctorRegistrationView(CreateAPIView):

    serializer_class = DoctorRegistrationSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message': 'Doctor registered  successfully',
            }
        status_code = status.HTTP_200_OK
        return Response(response, status=status_code)


class NurseRegistrationView(CreateAPIView):

    serializer_class = NurseRegistrationSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message': 'Nurse registered  successfully',
            }
        status_code = status.HTTP_200_OK
        return Response(response, status=status_code)

class UserLoginView(RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = {
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message': 'User logged in  successfully',
            'token' : serializer.data['token'],
            }
        status_code = status.HTTP_200_OK

        return Response(response, status=status_code)
