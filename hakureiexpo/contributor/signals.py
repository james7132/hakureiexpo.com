from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from contributor.models import Contributor


@receiver(post_save, sender=User)
def create_contributor(sender, instance, created, **kwargs):
    if created and not hasattr(instance, 'contributor'):
        Contributor.objects.create(user=instance)

        # Display name defaults to email address
        instance.contributor.display_name = instance.email


@receiver(post_save, sender=User)
def save_contributor(sender, instance, **kwargs):
    if hasattr(instance, 'contributor'):
        instance.contributor.save()
