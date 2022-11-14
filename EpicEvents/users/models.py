from django.contrib.auth.models import AbstractUser
from django.db import models

team = [("MANAGEMENT", "MANAGEMENT"),
        ("SALES", "SALES"),
        ("SUPPORT", "SUPPORT")]


# Create your models here.
class User(AbstractUser):
    team = models.CharField(choices=team, max_length=20, default='MANAGEMENT')

    def __str__(self):
        return "User" + "is" + self.username

    class Meta:
        ordering = ['id']

    # def is_superuser(self):
    #     pass