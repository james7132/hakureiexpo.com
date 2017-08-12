from django.db import models

# Create your models here.

class Submission(models.Model):
    name = models.CharField(max_length=1024)
    publish_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name
