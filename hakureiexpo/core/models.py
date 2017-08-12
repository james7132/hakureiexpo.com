from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Circle(models.Model):
    name = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.name


class User(AbstractUser):
    circles = models.ManyToManyField(Circle, related_name='members')


class Submission(models.Model):
    name = models.CharField(max_length=1024)
    publish_date = models.DateTimeField('date published')
    authors = models.ManyToManyField(Circle, related_name='submissions')

    def __str__(self):
        return self.name
