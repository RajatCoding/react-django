from django.db import models

# Create your models here.

class CustomUser(models.Model):
    print("hello")
    name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)

