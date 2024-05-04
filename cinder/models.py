from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=100)
    grade = models.IntegerField(default=10)
    section = models.CharField(max_length=1)
    gender = models.CharField(max_length=100)
    instagram = models.CharField(max_length=200, default="", blank=True)
    whatsapp = models.CharField(max_length=200, default="", blank=True)
    snapchat = models.CharField(max_length=200, default="", blank=True)
    other = models.CharField(max_length=200, default="", blank=True)
    interests = models.CharField(max_length=300)
    bio = models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.name

