from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View, generic
from .models import Pen

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

def index(request):
    return render(request, 'core/menu/trending.html')

def landing(request):
    return render(request, 'core/landing.html')

class PenCreateView(generic.CreateView):
    template_name = 'core/pen/create.html'
    model = Pen
    fields = ['title', 'description', 'public', 'html', 'css', 'js']
    success_url = reverse_lazy('core:pen-create') #change

    def form_valid(self, form):
        pen = form.save(commit=False)

        if self.request.user.is_authenticated:
            pen.owner = self.request.user
            pen.save()
        else:
            return redirect('accounts:login')
        return super().form_valid(form)

    # def get_success_url(self):
    #     return reverse_lazy('app:book-detail', kwargs={'pk':self.object.pk})
    
# class PenCreateView(View):
#     pass

# @method_decorator(login_required, name='dispatch')
# class PenCreateSubmit(View):
#     pass


