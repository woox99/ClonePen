from django.contrib.auth.models import User
from django.db import models

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     demo = models.BooleanField(default=False)
#     following = models.ManyToManyField(User, related_name='followers')
#     # bio = models.TextField(blank=True)
#     # avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
#     # location = models.CharField(max_length=100, blank=True)

#     def __str__(self):
#         return self.user.username