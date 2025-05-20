from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver


@receiver(post_save, sender=User)
def hash_user_password(sender, instance, created, **kwargs):
    if created and not instance.password.startswith('pbkdf2_sha256$'):
        instance.set_password(instance.password)
        instance.save()
