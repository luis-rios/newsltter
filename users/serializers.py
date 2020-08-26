#django
from django.contrib.auth import authenticate, password_validation

#django rest framework
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator

# models
from users.models import User


class BaseUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['names', 'email']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserLoginSerializer(serializers.Serializer):
	''' User Login Api View '''
	email =  serializers.EmailField()
	password = serializers.CharField(min_length=8)

	def validate(self, data):
		user = authenticate(username=data['email'], password=data['password'])
		if not user:
			raise serializers.ValidationError('Invalid credentials')
		self.context['user'] = user
		return data

	def create(self, data):
		token, created = Token.objects.get_or_created(user=self.context['user'])
		return self.context['user'], token.key


class UserSignUpSerializer(serializers.Serializer):
	''' User sign up serializer  '''

	email = serializers.EmailField(
		validators = [
			UniqueValidator(queryset=User.objects.all())
		]
	)

	names = serializers.CharField(
		max_length=50
	)

	last_name = serializers.CharField(
		max_length=50
	)

	password = serializers.CharField(
		min_length=8,
		max_length=64
	)

	password_confirmation = serializers.CharField(
		min_length=8,
		max_length=64
	)

	def validate(self, data):
		''' password verify match  '''
		password = data['password']
		password_conf = data['password_confirmation']
		if password != password_conf:
			raise serializers.ValidationError("Passwords don't match")
		password_validation.validate_password(password)
		return data

	def create(self, data):
		''' handle user creation '''
		data.pop('password_confirmation')
		user = User.objects.create_user(**data)
		return user

























