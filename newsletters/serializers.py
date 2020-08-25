from rest_framework import serializers

from newsletters.models import Newsletter


class BaseNewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = ['name', 'email']


class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = '__all__'
