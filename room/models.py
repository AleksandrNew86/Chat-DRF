from django.db import models
from sign.models import Writer


class Room(models.Model):
    writer = models.ManyToManyField(Writer)
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return str(self.name)


class Message(models.Model):
    writer = models.ForeignKey(Writer, on_delete=models.CASCADE)
    text = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return str(self.text)