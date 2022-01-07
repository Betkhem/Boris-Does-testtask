from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    name = models.CharField(max_length=255, blank=True)
    email      = models.EmailField(max_length=255, blank=True, unique=True)
    username   = models.CharField(max_length=255, blank=False, unique=True, null=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

