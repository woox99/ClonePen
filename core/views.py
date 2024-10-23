from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import Pen

def index(request):
    return render(request, 'core/menu/trending.html')

def landing(request):
    return render(request, 'core/landing.html')

# def create(request):
#     if request.method == 'POST':
#         owner = request.user
#         title = request.POST['title']
#         description = request.POST['description']
#         public = request.POST['public']
#         html = request.POST['html']
#         css = request.POST['css']
#         js = request.POST['js']
#         Pen.objects.create(
#             owner=owner,
#             title=title,
#             description=description,
#             public=public,
#             html=html,
#             css=css,
#             js=js,
#         )
#     return render(request, 'core/pen/create.html')

class PenCreateView(generic.CreateView):
    template_name = 'core/pen/create.html'
    model = Pen
    fields = ['title', 'description', 'public', 'html', 'css', 'js']
    success_url = reverse_lazy('core:pen-create') #change

    def form_valid(self, form):
        pen = form.save(commit=False)
        pen.owner = self.request.user
        pen.save()
        return super().form_valid(form)

    # def get_success_url(self):
    #     return reverse_lazy('app:book-detail', kwargs={'pk':self.object.pk})

