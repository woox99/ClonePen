from django.urls import path
from .views import *
from . import views

app_name='core'

urlpatterns=[
    # Menu
    path('', views.landing, name='landing-page' ),
    # path('trending/', views.index, name='trending' ),
    path('trending/', TrendingView.as_view(), name='trending' ),
    path('your-work/<str:username>/', YourWork.as_view(), name='your-work' ),

    # Pen
    path('pen/', PenCreateView.as_view(), name='pen-create' ),
    path('pen-url/<int:pk>/', PenURLView.as_view(), name='pen-url' ),
    path('pen/<slug:slug>/', PenDetailView.as_view(), name='pen-detail' ),
]