from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.db.models.signals import post_save
from django.dispatch import receiver


class Conversation(models.Model):
    participants = models.ManyToManyField(User, related_name='conversations')
    last_message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        participant_names = ", ".join([user.username for user in self.participants.all()])
        return f"Conversation between: {participant_names}"


class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender.username} in Conversation ID: {self.conversation.id}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    demo = models.BooleanField(default=False)
    following = models.ManyToManyField(User, related_name='followers')
    pinned_items = models.ManyToManyField('core.Pen', related_name='pinned_profiles') # String reference to avoid circular import
    last_conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, null=True, blank=True,)

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


class Pen(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='pens')
    title = models.CharField(max_length=30, blank=False) #change
    description = models.CharField(max_length=250, blank=True, null=True) #change
    public = models.BooleanField(default=False)
    html = models.TextField(blank=True, null=True)
    css = models.TextField(blank=True, null=True)
    js = models.TextField(blank=True, null=True)
    views = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=30, unique=True, blank=True)

    def get_absolute_url(self):
        return reverse_lazy('core:pen-detail', kwargs={'slug':self.slug})

    def __str__(self):
        return self.title
    
# Create slug field for any model that has slug attribute upon save()
@receiver(pre_save)
def generate_slug(sender, instance, **kwargs):
    if hasattr(instance, 'slug') and hasattr(instance, '__str__'):
        slug = slugify(instance.__str__())
        base_slug = slug
        counter = 2
        while sender.objects.filter(slug=slug).exists():
            slug = f'{base_slug}-{counter}'
            counter += 1
        instance.slug = slug 


    

    
# class Comment(models.Model):
#     owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
#     pen = models.ForeignKey(Pen, on_delete=models.CASCADE, related_name='comments')
#     content = models.TextField(max_length=250) #change
#     created = models.DateTimeField(auto_now_add=True)
#     modified = models.DateTimeField(auto_now=True)
    
#     def __str__(self):
#         return f"{self.owner} commented on {self.pen}: {self.content[:20]}..."

# class Reply(models.Model):
#     owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='replies')
#     comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')
#     content = models.TextField(max_length=250) #change
#     created = models.DateTimeField(auto_now_add=True)
#     modified = models.DateTimeField(auto_now=True)
    
#     def __str__(self):
#         return f"{self.owner} replied to {self.comment.owner}'s comment: {self.content[:20]}..."

