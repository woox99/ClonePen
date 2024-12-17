from django.contrib.auth.models import User
from django.db import models
from core.models import Pen
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    demo = models.BooleanField(default=False)
    following = models.ManyToManyField(User, related_name='followers')
    pens = models.ManyToManyField(Pen)
    # bio = models.TextField(blank=True)
    # avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    # location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username
    

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    # only execute if instance created (true), not updated (false)
    if created:
        Profile.objects.create(user=instance)