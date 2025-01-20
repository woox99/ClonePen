from django.urls import path
from .views import *
from . import views

app_name='core'

urlpatterns=[
    path('', views.landing, name='landing-page' ),
    path('trending/', TrendingView.as_view(), name='trending' ),
    path('profile/<str:username>/grid-view/', ProfileView.as_view(), name='profile' ),
    # path('profile/<str:username>/list-view/', ProfileListView.as_view(), name='profile-list' ),
    path('your-work/list-view/<str:username>/', YourWorkListView.as_view(), name='your-work-list' ),
    path('your-work/grid-view/<str:username>/', YourWorkGridView.as_view(), name='your-work-grid' ),
    path('messages/<str:username>/', MessagesView.as_view(), name='messages' ),
    path('chat/<int:pk>/', ChatView.as_view(), name='chat' ),
    path('pen/', PenCreateView.as_view(), name='pen-create' ),
    path('pen/<slug:slug>/', PenDetailView.as_view(), name='pen-detail' ),
    path('edit-pen/<slug:slug>/', PenUpdateView.as_view(), name='pen-update' ),
    path('delete-pen/<int:pk>/', PenDeleteView.as_view(), name='pen-delete' ),
]