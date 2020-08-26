# django
from django.shortcuts import render

# django rest framework
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import status

# models
from users.models import User

# serializers
from users.serializers import (
	UserSerializer, 
	UserLoginSerializer,
	UserSignUpSerializer
)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserLoginAPIView(APIView):
	''' User Login View '''
	def post(self, request, *args, **kwargs):
		serializer = UserLoginSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user, token = serializer.save()
		data = {
			'user' : UserSerializer(User).data,
			'access_token' : token
		}
		return Response(data, status=status.HTTP_201_CREATED)


class UserSignUpAPIView(APIView):
	''' User Signup View '''
	def post(self, request, *args, **kwargs):
		serializer = UserSignUpSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user, token = serializer.save()
		data = UserSerializer(User).data
		return Response(data, status=status.HTTP_201_CREATED)
		
