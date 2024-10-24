from django.db import models
from django.contrib.auth.models import User

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

    def __str__(self):
        return self.title

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
