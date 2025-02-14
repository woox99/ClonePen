from django.urls import path
from .views import *

app_name='api'

urlpatterns=[
    path('toggle-pin/<int:pk>/', TogglePin.as_view()),
    path('toggle-follow/<int:profile_id>/', ToggleFollow.as_view()),
    # path('get-pinned-items/', GetPinnedItemsByActiveUser.as_view()),
    path('messages/unread-count/', GetUnreadMessageCount.as_view()),
]