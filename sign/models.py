from django.db import models
from django.contrib.auth.models import User


class Writer(models.Model):
    writer = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=64, unique=True)
    avatar = models.ImageField(null=True, blank=True, upload_to="images/profile/")

    def __str__(self):
        return str(self.name)
