from django.db import models

# Create your models here.

class CustomUser(models.Model):
    name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    name = models.CharField(max_length=100)
