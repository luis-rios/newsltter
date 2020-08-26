from django.urls import include, path
from rest_framework.routers import DefaultRouter

from tags.views import TagViewSet

router = DefaultRouter()
router.register(r'Tag', TagViewSet)

urlpatterns = [
    path('', include(router.urls))
]