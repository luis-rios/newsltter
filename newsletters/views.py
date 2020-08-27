from django.shortcuts import render
from rest_framework import viewsets

from newsletters.models import Newsletter
from newsletters.serializers import NewsletterSerializer, BaseNewsletterSerializer


class NewsletterViewSet(viewsets.ModelViewSet):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer

    def get_queryset(self):
        parameters = {}
        for param in self.request.query_params:
            if param in ['page', 'page_size']:
                continue
            if param in ['tags', 'newsletter', 'id']:
                continue
            newsletter_filtered = Newsletter.objects.filter(**parameters)
            return newsletter_filtered

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return BaseNewsletterSerializer
        return NewsletterSerializer
