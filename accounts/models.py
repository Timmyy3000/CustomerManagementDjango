from django.db import models
from django.db.models.fields import CharField


class Customer (models.Model):

    name = models.CharField(max_length = 200, null=True)
    email = models.CharField(max_length = 200, null=True)
    phone = models.CharField(max_length = 200, null=True)
    date_created = models.DateTimeField(auto_now_add=True)