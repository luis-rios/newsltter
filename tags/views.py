from django.shortcuts import render
from rest_framework import viewsets

from tags.models import Tag
from tags.serializers import TagSerializer, BaseTagSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def get_queryset(self):
        parameters = {}
        for param in self.request.query_params:
            if param in ['page', 'page_size']:
                continue
            if param in ['tags', 'newsletter', 'id']:
                continue
            tags_filtered = Tag.objects.filter(**parameters)
            return tags_filtered

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return BaseTagSerializer
        return TagSerializer

