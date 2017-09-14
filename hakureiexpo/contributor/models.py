from django.db import models
from django.contrib.auth.models import User


class Contributor(models.Model):
    user = models.OneToOneField(User)
    image = models.ImageField()
    display_name = models.CharField(max_length=256)
    # todo: add social links
