from django.shortcuts import render
from rest_framework import viewsets

from newsletters.models import Newsletter
from newsletters.serializers import NewsletterSerializer


class NewsletterViewSet(viewsets.ModelsViewSet):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer

