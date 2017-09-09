from django.db import models
from django.utils.crypto import get_random_string

from contributor.models import Contributor

def populate_circle_slug():
    while True:
        slug = get_random_string(8)
        if not Circle.objects.filter(slug=slug).exists():
            return slug


def circle_image_upload(instance, filename):
    return "circle/{0}/{1}".format(instance.slug, filename)


class Circle(models.Model):
    slug = models.CharField(max_length=8, default=populate_circle_slug)
    name = models.CharField(max_length=256, unique=True)
    contributors = models.ManyToManyField(Contributor)
    image = models.ImageField(upload_to=circle_image_upload)

    def __str__(self):
        return self.name
