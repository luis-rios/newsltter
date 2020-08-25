from django.contrib.auth.models import User
from django.db import models


class Newsletter(models.Models):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=80)
    password = models.CharField(max_length=20)
    creation_date = models.DateField()
    user = models.ManyToManyField(User, on_delate=models.CASCADE, related_name='subscribe')

    def __str__(self):
        return self.name
