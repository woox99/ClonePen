from django.urls import path
from .views import *
from . import views

app_name='core'

urlpatterns=[
    path('', views.landing, name='landing-page' ),
    path('trending/', TrendingView.as_view(), name='trending' ),
    path('pinned-items/', PinnedItemsView.as_view(), name='pinned-items' ),
    path('following/', FollowingView.as_view(), name='following' ),
    path('search', SearchView.as_view(), name='search' ),
    # path('profile/<str:username>/list-view/', ProfileListView.as_view(), name='profile-list' ),
    path('messages/', MessagesView.as_view(), name='messages' ),
    path('chat/', ChatView.as_view(), name='chat' ),
    path('create-message/<int:pk>/', MessageCreateView.as_view(), name='message-create' ),
    path('create-chat/<int:sender_pk>/<int:receiver_pk>/', ChatCreateView.as_view(), name='chat-create' ),
    path('create-pen/', PenCreateView.as_view(), name='pen-create' ),
    path('pen/<slug:slug>/', PenDetailView.as_view(), name='pen-detail' ),
    path('edit-pen/<slug:slug>/', PenUpdateView.as_view(), name='pen-update' ),
    path('delete-pen/<int:pk>/', PenDeleteView.as_view(), name='pen-delete' ),
    path('profile/<str:username>/list-view/', ProfileListView.as_view(), name='profile-list-view' ),
    path('profile/<str:username>/', ProfileView.as_view(), name='profile' ), ### Keep at bottom
]