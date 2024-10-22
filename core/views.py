from django.shortcuts import render
from django.views import generic

def index(request):
    return render(request, 'core/trending.html')

def landing(request):
    return render(request, 'core/landing.html')

def create(request):
    if request.method == 'POST':
        print(request.POST)
    return render(request, 'core/create.html')
