from django.contrib.auth.models import User
from django.db import models


class Newsletter(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=80)
    password = models.CharField(max_length=20)
    creation_date = models.DateField()
    user = models.ManyToManyField(User, related_name='subscribe')

    def __str__(self):
        return self.name
