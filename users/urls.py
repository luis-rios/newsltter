from django.urls import include, path
from rest_framework.routers import DefaultRouter

from users.views import (
	UserViewSet, 
	UserLoginAPIView,
	UserSignUpAPIView
)


router = DefaultRouter()
router.register(r'User', UserViewSet)


urlpatterns = [
	path('users/login/', UserLoginAPIView.as_view(), name='login'),
	path('users/signup/', UserSignUpAPIView.as_view(), name='signup'),
	path('', include(router.urls))
]