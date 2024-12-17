from django.urls import path
from .views import *

app_name='api'

urlpatterns=[
    path('toggle-pin/<int:pk>/', TogglePin.as_view())
]