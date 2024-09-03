from django.db import models
from django.contrib.auth.models import User

class PersonalToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=255)

    def __str__(self):
        return self.user.email


# Create your models here.
