from django.shortcuts import render, get_object_or_404
from django.views import View
from core.models import Pen
from django.http import JsonResponse, HttpResponse
from api.serializers import *


class TogglePin(View):
    def post(self, request, pk):
        pen = get_object_or_404(Pen, pk=pk)
        if pen in request.user.profile.pinned_items.all():
            request.user.profile.pinned_items.remove(pen)
            return JsonResponse({'pinned': False})
        request.user.profile.pinned_items.add(pen)
        return JsonResponse({'pinned': True})

class GetPinnedItemsByActiveUser(View):
    def post(self, request):
        # fetch only public pinned items
        pinned_items = request.user.profile.pinned_items.filter(public=True)
        serialized_pinned_items = PenSerializer(pinned_items, many=True)
        return JsonResponse({'pinned-items': serialized_pinned_items.data})

