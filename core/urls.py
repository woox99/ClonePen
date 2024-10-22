from django.urls import path
from .views import *
from . import views

app_name='core'

urlpatterns=[
    path('', views.landing, name='landing-page' ),
    path('trending/', views.index, name='trending' ),
    path('create/', views.create, name='create' ),
]