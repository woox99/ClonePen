from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View, generic
from django.db.models import F, Q
from django.http import Http404
from .models import *
from django.contrib.auth.models import User
from .forms import PenForm

from django.core.paginator import Paginator

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class TrendingView(generic.ListView):
    template_name = 'core/menu/trending.html'
    model = Pen

    def get_context_data(self):
        pens = Pen.objects.filter(is_public=True).order_by('-modified')
        paginator = Paginator(pens, 4)
        page_number = self.request.GET.get('page')
        if not page_number:
            next_page_number = 2
        else:
            next_page_number = str(int(page_number) + 1)
        page_object = paginator.get_page(page_number)
        next_page_object = paginator.get_page(next_page_number)
        context = {
            'page_object':page_object,
            'next_page_object':next_page_object,
            }
        return context


class PinnedItemsView(generic.ListView):
    template_name = 'core/menu/pinned_items.html'
    model = Pen

    def get_context_data(self):
        # pens = Pen.objects.filter(is_public=True).order_by('-modified')
        pens = self.request.user.profile.pinned_items.filter(is_public=True)
        paginator = Paginator(pens, 4)
        page_number = self.request.GET.get('page')
        if not page_number:
            next_page_number = 2
        else:
            next_page_number = str(int(page_number) + 1)
        page_object = paginator.get_page(page_number)
        next_page_object = paginator.get_page(next_page_number)
        context = {
            'page_object':page_object,
            'next_page_object':next_page_object,
            }
        return context


class SearchView(View):
    def get(self, request):
        query = request.GET.get('q', '')
        pens = Pen.objects.filter( Q(title__icontains=query) | Q(owner__username__icontains=query), is_public=True)

        paginator = Paginator(pens, 4)
        page_number = self.request.GET.get('page')
        if not page_number:
            next_page_number = 2
        else:
            next_page_number = str(int(page_number) + 1)
        page_object = paginator.get_page(page_number)
        next_page_object = paginator.get_page(next_page_number)
        context = {
            'page_object':page_object,
            'next_page_object':next_page_object,
            'query':query,
            }
        return render(request, 'core/menu/search.html', context=context)


class FollowingView(generic.ListView):
    template_name = 'core/menu/following.html'
    model = Pen

    def get_context_data(self):
        following_profile_set = self.request.user.profile.following.all()
        following_user_set = User.objects.filter(profile__in=following_profile_set)
        pens = Pen.objects.filter(owner__in=following_user_set).filter(is_public=True).order_by('-modified')

        paginator = Paginator(pens, 4)
        page_number = self.request.GET.get('page')
        if not page_number:
            next_page_number = 2
        else:
            next_page_number = str(int(page_number) + 1)
        page_object = paginator.get_page(page_number)
        next_page_object = paginator.get_page(next_page_number)
        context = {
            'page_object':page_object,
            'next_page_object':next_page_object,
            }
        return context


class ProfileView(View):
    def get(self, request, username):
        profile = get_object_or_404(Profile, user__username=username)

        # If user is on their own profile get all pens, else only public pens
        if request.user.profile == profile:
            pens = Pen.objects.filter(owner=profile.user).order_by('-modified')
        else:
            pens = Pen.objects.filter(owner=profile.user).filter(is_public=True).order_by('-modified')

        paginator = Paginator(pens, 4)
        page_number = self.request.GET.get('page')
        if not page_number:
            next_page_number = 2
        else:
            next_page_number = str(int(page_number) + 1)
        page_object = paginator.get_page(page_number)
        next_page_object = paginator.get_page(next_page_number)

        context = {
            'page_object':page_object,
            'next_page_object':next_page_object,
            'profile':profile,
            }
        return render(request, 'core/menu/profile.html', context=context)


class ProfileListView(View):
    def get(self, request, username):
        profile = get_object_or_404(Profile, user__username=username)

        # If user is on their own profile get all pens, else only public pens
        if request.user.profile == profile:
            pens = Pen.objects.filter(owner=profile.user).order_by('-modified')
        else:
            pens = Pen.objects.filter(owner=profile.user).filter(is_public=True).order_by('-modified')

        return render(request, 'core/menu/profile_list_view.html', {'pens':pens, 'profile':profile})





# change to cbf
def landing(request):
    return render(request, 'core/menu/landing.html')


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
                return redirect('core:profile', username=request.user.username)
        return render(request, 'core/pen/create.html', {'form':form})


class PenDetailView(generic.DetailView):
    template_name = 'core/pen/detail.html'
    model = Pen

    def get_object(self):
        pen = super().get_object()
        # Increment the view count atomically
        Pen.objects.filter(pk=pen.pk).update(views=F('views') + 1)
        # Refresh the pen instance to reflect updated view count
        pen.refresh_from_db()
        return pen


class PenUpdateView(generic.UpdateView):
    model = Pen
    fields = ['title', 'description', 'html', 'css', 'js', 'is_public']
    template_name = 'core/pen/update.html'

    def get_success_url(self):
        return reverse_lazy('core:profile', kwargs={'username':self.request.user.username})


class PenDeleteView(View):
    def post(self, request, pk):
        pen = get_object_or_404(Pen, pk=pk)
        if request.user == pen.owner:
            pen.delete()
            return redirect('core:profile', username=request.user.username)
        else:
            raise Http404() # Create 404 view


class MessagesView(View):
    def get(self, request):
        conversations = request.user.conversations.order_by('-modified')
        last_conversation = request.user.profile.last_conversation

        # Sets request user so other participant can be used in template
        for conversation in conversations:
            conversation.set_request_user(request.user)
        if last_conversation:
            last_conversation.set_request_user(request.user)

        # Sets unread messages to read if last conversation exists && sender is not current user
        if last_conversation and last_conversation.messages.last().is_read == False:
            unread_messages = last_conversation.messages.filter(is_read = False)
            for message in unread_messages:
                if message.sender != request.user:
                    message.is_read = True
                    message.save()
        return render(request, 'core/menu/messages.html', {'conversations':conversations, 'chat':last_conversation})

class ChatView(View):
    def post(self, request):
        chat = get_object_or_404(Conversation, pk=request.POST['conversation_id'])
        request.session['conversation_id'] = chat.pk

        chat.set_request_user(request.user)
        return redirect(f'/clonepen.com/chat/#{chat.other_participant}')
    
    def get(self, request):
        chat_id = request.session.get('conversation_id')
        chat = get_object_or_404(Conversation, pk=chat_id)
        conversations = request.user.conversations.order_by('-modified')
        
        # Sets request user so other participant can be used in template
        for conversation in conversations:
            conversation.set_request_user(request.user)
        chat.set_request_user(request.user)

        profile = get_object_or_404(Profile, user=request.user)
        profile.last_conversation = chat
        profile.save()

        unread_messages = chat.messages.filter(is_read = False)
        for message in unread_messages:
            if message.sender != request.user:
                message.is_read = True
                message.save()
        return render(request, 'core/menu/chat.html', {'conversations':conversations, 'chat':chat})

class MessageCreateView(View):
    def post(self, request, pk):
        conversation = get_object_or_404(Conversation, pk=pk)
        content = request.POST['content']
        if len(content) == 0:
            content = '[empty message]'
        conversation.last_message = content
        conversation.save()
        conversation.set_request_user(request.user)
        Message.objects.create(conversation=conversation, content=content, sender=request.user)
        return redirect(f'/clonepen.com/chat/#{conversation.other_participant}')
    

class ChatCreateView(View):
    def post(self, request, sender_pk, receiver_pk):
        sender = get_object_or_404(User, pk=sender_pk)
        receiver = get_object_or_404(User, pk=receiver_pk)
        content = request.POST['content']
        if len(content) == 0:
            content = '[empty message]'
        conversation = Conversation.objects.filter(participants=sender).filter(participants=receiver).first()
        if not conversation:
            conversation = Conversation.objects.create(last_message=content)
            conversation.participants.set([sender, receiver])
            conversation.save()
        conversation.set_request_user(request.user)
        Message.objects.create(sender=sender, content=content, conversation=conversation)
        return redirect(f'/clonepen.com/chat/#{conversation.other_participant}')




