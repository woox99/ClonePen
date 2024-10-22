from django.shortcuts import render
from django.contrib.auth import login
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.views.generic import FormView
from .forms import RegisterForm

from django.http import JsonResponse

class UserLogin(LoginView):
    template_name = 'registration/login.html'
    
    def get_success_url(self):
        # next_url = self.request.GET.get('next')
        # if next_url:
        #     return next_url
        # return reverse_lazy('app:dashboard')
        return reverse_lazy('core:trending')
    
class UserLogout(LogoutView):
    next_page = reverse_lazy('core:landing-page')


class UserRegister(FormView):
    template_name = 'registration/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('core:trending')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

