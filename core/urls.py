from django.urls import path
from .views import *
from . import views

app_name='core'

urlpatterns=[
    # Menu
    path('', views.landing, name='landing-page' ),
    # path('trending/', views.index, name='trending' ),
    path('trending/', TrendingView.as_view(), name='trending' ),

    # Pen
    path('pen/', PenCreateView.as_view(), name='pen-create' ),
]