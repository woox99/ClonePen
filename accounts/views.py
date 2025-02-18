from django.shortcuts import render
from django.contrib.auth import login
from django.urls import reverse_lazy
from core.models import Profile

from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.views.generic import FormView
from .forms import RegisterForm
from django.http import JsonResponse

import random

class UserLogin(LoginView):
    template_name = 'registration/login.html'
    
    def get_success_url(self):
        next_url = self.request.session.get('next_url')
        if next_url:
            return next_url
        return reverse_lazy('core:trending')


class UserLogout(LogoutView):
    next_page = reverse_lazy('core:landing-page')


class UserRegister(FormView):
    template_name = 'registration/register.html'
    form_class = RegisterForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
    
    def get_success_url(self):
        next_url = self.request.session.get('next_url')
        if next_url:
            return next_url
        return reverse_lazy('core:trending')
    

# class DemoAccount():
    
#     pass
    
