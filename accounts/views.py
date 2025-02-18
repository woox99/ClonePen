from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse_lazy
from core.models import Profile
from django.views import View


from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.views.generic import FormView
from .forms import RegisterForm
from django.http import JsonResponse

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
    

class CreateDemoAccount(View):
    def get(self, request):
        if request.user.is_authenticated: 
            return redirect('core:trending')
        demo_count = len(Profile.objects.filter(is_demo=True))
        username = f'DemoAccount_' + str(demo_count)
        while User.objects.filter(username=username).exists():
            demo_count += 1
            username = f'DemoAccount#' + str(demo_count)
        demo_account = User.objects.create(username=username)
        profile = Profile.objects.get(user=demo_account)
        profile.is_demo = True
        profile.save()
        login(request, demo_account)
        return redirect('core:trending')
