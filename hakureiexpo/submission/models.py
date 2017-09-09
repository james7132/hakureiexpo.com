from django.contrib.auth.models import User
from django.db import models
from django.utils.crypto import get_random_string

from circle.models import Circle
from contributor.models import Contributor


def populate_submission_slug():
    while True:
        slug = get_random_string(8)
        if not Submission.objects.filter(slug=slug).exists():
            return slug


def submission_image_upload(instance, filename):
    return "submissions/{0}/{1}".format(instance.slug, filename)


class SubmissionType(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class SubmissionSubType(models.Model):
    name = models.CharField(max_length=256)
    type = models.ForeignKey(SubmissionType)

    def __str__(self):
        return self.name


class Submission(models.Model):
    slug = models.CharField(max_length=8, default=populate_submission_slug)
    title = models.CharField(max_length=256)
    description = models.TextField()
    image = models.ImageField(upload_to=submission_image_upload)
    publish_date = models.DateTimeField(auto_now_add=True)
    external_link = models.URLField()
    circle = models.ForeignKey(Circle, null=True, blank=True, related_name='submissions')
    contributors = models.ManyToManyField(Contributor)
    # TODO: event? we can add this later
    type = models.ForeignKey(SubmissionType)
    subtype = models.ForeignKey(SubmissionSubType)
    # TODO: Tags
    is_public = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

    @property
    def absolute_url(self):
        return reverse('submission:detail', kwargs={'slug': self.slug})

class SubmissionLike(models.Model):
    submission = models.ForeignKey(Submission)
    user = models.ForeignKey(User)


class SubmissionComment(models.Model):
    submission = models.ForeignKey(Submission)
    user = models.ForeignKey(User)
    comment = models.TextField()
    comment_time = models.DateTimeField(auto_now_add=True)
