from django.shortcuts import render, get_object_or_404
from django.views import View
from core.models import Pen, Message
from django.http import JsonResponse, HttpResponse
from api.serializers import *

# Toggle pin button that saves/unsaves Pens to 'Pinned Items'
class TogglePin(View):
    def post(self, request, pk):
        pen = get_object_or_404(Pen, pk=pk)
        if pen in request.user.profile.pinned_items.all():
            request.user.profile.pinned_items.remove(pen)
            return JsonResponse({'pinned': False})
        request.user.profile.pinned_items.add(pen)
        return JsonResponse({'pinned': True})

# Fetch all pinned items by current user
class GetPinnedItemsByActiveUser(View):
    def post(self, request):
        # fetch only public pinned items
        pinned_items = request.user.profile.pinned_items.filter(public=True)
        serialized_pinned_items = PenSerializer(pinned_items, many=True)
        return JsonResponse({'pinned-items': serialized_pinned_items.data})

# Fetch unread message count
class GetUnreadMessageCount(View):
    def get(self, request):
        messages = Message.objects.filter(conversation__participants=request.user)
        unread_count = messages.filter(is_read=False).exclude(sender=request.user).count()
        return JsonResponse({'unread_count': unread_count})