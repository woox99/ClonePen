from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver

class Pen(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pens')
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

