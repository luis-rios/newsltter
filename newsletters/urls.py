from django.urls import include, path
from rest_framework.routers import DefaultRouter

from newsletters.views import NewsletterViewSet

router = DefaultRouter()
router.register(r'Newsletter', NewsletterViewSet)

app_name = 'newsletters'
urlpatterns = [
    path('', include(router.urls)),

]