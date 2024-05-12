from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    # Add your additional fields here
    date_of_birth = models.DateField(blank=True, null=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.username