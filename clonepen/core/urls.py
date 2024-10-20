from django.urls import path
from .views import * #remove

app_name='core'

urlpatterns=[
    path('', landing, name='landing-page' ),
    path('trending/', index, name='index' ),
]