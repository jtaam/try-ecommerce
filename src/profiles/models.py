from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(default='description default text')

    def __str__(self):
        return self.name
