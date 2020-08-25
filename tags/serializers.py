from rest_framework import serializers

from tags.models import Tag


class BaseTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
