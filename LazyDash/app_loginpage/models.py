from django.db import models

class Users(models.Model):
    login = models.CharField(max_length=150, unique=True)
    senha = models.CharField(max_length=128)