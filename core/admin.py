from django.contrib import admin
from core.models import *

class ProfileAdmin(admin.ModelAdmin):
    # adds field column on model list page
    list_display = ['user', 'id', 'demo']

#     # adds filter box on model list page
#     list_filter = ['publisher', 'published_date']

#     # groups fields together with different fieldsets
#     fieldsets = [
#         ('Book Details', {"fields": ["title", 'publisher', 'authors', 'pages']}),
#         ("Date information", {"fields": ["published_date"]}),
#     ]

admin.site.register(Pen)
admin.site.register(Conversation)
admin.site.register(Message)
admin.site.register(Profile, ProfileAdmin)