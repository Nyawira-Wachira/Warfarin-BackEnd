from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class HelloView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = (IsAuthenticated,)
  
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)