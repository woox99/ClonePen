from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View, generic
from .models import Pen
from .forms import PenForm

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

def index(request):
    return render(request, 'core/menu/trending.html')


def landing(request):
    return render(request, 'core/landing.html')


class PenCreateView(View):
    def get(self, request):
        # retrieve pen data from session if login/register was required 
        form_data = request.session.get('pen_form')
        if form_data:
            form = PenForm(form_data)
        else:
            form = PenForm()
        return render(request, 'core/pen/create.html', {'form':form})
    
    def post(self, request):
        if not request.user.is_authenticated:
            # save pen data and path in session if login/register required
            form_data = {
                'title':request.POST['title'],
                'description':request.POST['description'],
                'html':request.POST['html'],
                'css':request.POST['css'],
                'js':request.POST['js'],
            }
            request.session['pen_form'] = form_data
            next_url = request.path
            request.session['next_url'] = next_url
            login_url = reverse_lazy('accounts:login')
            return redirect(f"{login_url}?next={next_url}")
        else:
            form = PenForm(data=request.POST)
            if request.session.get('pen_form'):
                del request.session['pen_form']
            if form.is_valid():
                pen = form.save(commit=False)
                pen.owner = request.user
                pen.save()
                return redirect('core:trending') #change to pen-detail-view
        return render(request, 'core/pen/create.html', {'form':form})



