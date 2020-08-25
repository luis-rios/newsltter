from django.db import models

from newsletters.models import Newsletter


class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)
    creation_date = models.DateField()
    newsletter = models.ManyToManyField(Newsletter, on_delate=models.CASCADE, related_name='tag')

    def __str__(self):
        return self.name
