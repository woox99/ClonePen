from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save, pre_delete
from django.dispatch import receiver
from django.utils.timesince import timesince
from django.utils.timezone import now
from datetime import timedelta



class Pen(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pens')
    title = models.CharField(max_length=30, blank=False) #change
    description = models.CharField(max_length=250, blank=True, null=True) #change
    is_public = models.BooleanField(default=False)
    html = models.TextField(blank=True, null=True)
    css = models.TextField(blank=True, null=True)
    js = models.TextField(blank=True, null=True)
    views = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True)

    @property
    def modified_timestamp(self):
        return create_timestamp(self.modified)

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


class Conversation(models.Model):
    participants = models.ManyToManyField(User, related_name='conversations')
    last_message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    @property
    def timestamp(self):
        return create_timestamp(self.modified)
    
    @property
    def other_participant(self):
        request_user = getattr(self, '_current_user', None)
        if request_user:
            return self.participants.exclude(id=request_user.id).first()
        return None
    
    def set_request_user(self, current_user):
        # sets an attribute to the model
        self._current_user = current_user

    def __str__(self):
        participant_names = ", ".join([user.username for user in self.participants.all()])
        return f"Conversation between: {participant_names}"


class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    content = models.TextField()
    is_read = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    @property
    def timestamp(self):
        return create_timestamp(self.created)

    def __str__(self):
        return f"Message from {self.sender.username} in Conversation ID: {self.conversation.id}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    is_demo = models.BooleanField(default=False)
    following = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    pinned_items = models.ManyToManyField('core.Pen', related_name='pinned_profiles') # String reference to avoid circular import
    last_conversation = models.ForeignKey(Conversation, on_delete=models.SET_NULL, null=True, blank=True,)

    # bio = models.TextField(blank=True)
    # avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    # location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username
    

# Create profile for user when sender=User is created
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    # only execute if instance created (true), not updated (false)
    if created:
        Profile.objects.create(user=instance)


# Create welcome message from ClonePen to new user when sender=User is created
@receiver(post_save, sender=User)
def create_message(sender, instance, created, **kwargs):
    # only execute if instance created (true), not updated (false)
    if created:
        clonepen = User.objects.filter(username='ClonePen').first()
        first_message = 'Welcome to ClonePen! You can message our team here if you need support. \
                        This application is a clone of CodePen. We are not affiliated with ClonePen in anyway, nor are we trying to pose as the offical site.'
        conversation = Conversation.objects.create(last_message=first_message)
        conversation.participants.set([clonepen, instance])
        Message.objects.create(conversation=conversation, sender=clonepen, content=first_message)


# Cascade deleting user to deleting conversation
@receiver(pre_delete, sender=User)
def delete_related_conversation(sender, instance, **kwargs):
    conversations = Conversation.objects.filter(participants=instance)
    for conversation in conversations:
        conversation.delete()


# Creates a shorthand timestamp
def create_timestamp(date):
    delta = now() - date
    
    if delta < timedelta(minutes=1):
        return "Now"
    elif delta < timedelta(hours=1):
        return f"{delta.seconds // 60}m"
    elif delta < timedelta(days=1):
        return f"{delta.seconds // 3600}h"
    elif delta < timedelta(days=365):
        return f"{delta.days}d"
    else:
        years = delta.days // 365
        return f"{years}y"


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

