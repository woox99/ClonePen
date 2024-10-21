from django.urls import path
from .views import *

app_name='accounts'

urlpatterns=[
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', UserLogout.as_view(), name='logout'),
    path('sign-up/', UserRegister.as_view(), name='register'),
]