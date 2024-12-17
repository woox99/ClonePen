from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    demo = models.BooleanField(default=False)
    following = models.ManyToManyField(User, related_name='followers')
    pinned_items = models.ManyToManyField('core.Pen', related_name='pinned_profiles') # String reference to avoid circular import
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