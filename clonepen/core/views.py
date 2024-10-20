from django.shortcuts import render

def index(request):
    return render(request, 'core/trending.html')

def landing(request):
    return render(request, 'core/landing.html')